import gc
import os
import socket
import struct
import sys
import threading
import time
import traceback

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog


class fileTransfers(QMainWindow):
    sigUpdateSpeed = pyqtSignal(dict)  # 更新进度速度

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600, 300)
        self.InitUI()
        self.show()
        self.downTh = threading.Thread(target=self.Test)
        self.downTh.start()
        self.uploadTh = threading.Thread(target=self.Test)
        self.uploadTh.start()
        self.sigUpdateSpeed.connect(self.sigUpdateSpeedDo)
    def Test(self):
        pass


    def InitUI(self):
        self.checkDirBtn = QPushButton(self)
        self.checkDirBtn.setGeometry(10, 5, 100, 30)
        self.checkDirBtn.setText("选取文件夹上传")
        self.checkDirBtn.clicked.connect(self.checkDir)

        self.downBtn = QPushButton(self)
        self.downBtn.setGeometry(150, 5, 100, 30)
        self.downBtn.setText("下载")
        self.downBtn.clicked.connect(self.down)

        self.nowModeShow = QLabel(self)   # 当前模式
        self.nowModeShow.setGeometry(10, 75, 600, 15)
        self.nowModeShow.setText("当前模式：上传")

        self.nowFilesShow = QLabel(self)   # 当前文件
        self.nowFilesShow.setGeometry(10, 100, 600, 15)
        self.nowFilesShow.setText("当前文件：dfsdsdsdsssssssssssssssssssssssssssssss")

        self.nowFilesShow2 = QLabel(self)  # 当前文件大小
        self.nowFilesShow2.setGeometry(10, 125, 600, 15)
        self.nowFilesShow2.setText("当前文件：dfsdsdsdsssssssssssssssssssssssssssssss")

        self.progressLabel1 = QLabel(self)   # 进度条底层
        self.progressLabel1.setGeometry(10, 150, 454, 15)
        self.progressLabel1.setStyleSheet("QLabel{background-color:rgb(200, 200, 200)}")

        self.progressLabel2 = QLabel(self)   # 进度条顶层
        self.progressLabel2.setGeometry(12, 152, 0, 11)
        self.progressLabel2.setStyleSheet("QLabel{background-color:rgb(200, 100, 100)}")

        self.speedShow = QLabel(self)          # 速度显示
        self.speedShow.setGeometry(468, 150, 100, 15)
        self.speedShow.setText("100MB/s")

        self.progressShow = QLabel(self)        # 进度显示，与顶层进度条一起走
        self.progressShow.setGeometry(230, 150, 50, 15)
        self.progressShow.setText("56%")

        self.TotalFileNums = QLabel(self)
        self.TotalFileNums.setGeometry(10, 50, 600, 15)
        self.TotalFileNums.setText("文件总数: 12")

        self.progressLabel3 = QLabel(self)  # 进度条底层
        self.progressLabel3.setGeometry(10, 172, 454, 15)
        self.progressLabel3.setStyleSheet("QLabel{background-color:rgb(200, 200, 200)}")

        self.progressLabel4 = QLabel(self)
        self.progressLabel4.setGeometry(12, 172, 0, 11)
        self.progressLabel4.setStyleSheet("QLabel{background-color:rgb(200, 100, 100)}")

        self.speedShow2 = QLabel(self)
        self.speedShow2.setGeometry(468, 170, 100, 15)
        self.speedShow2.setText("120MB/s")

        self.progressShow2 = QLabel(self)  # 进度显示，与顶层进度条一起走
        self.progressShow2.setGeometry(230, 170, 50, 15)
        self.progressShow2.setText("12%")

    def sigUpdateSpeedDo(self, datas):
        self.speedShow.setText(datas["speed"])
        self.progressShow.setText(datas["progress"])
        self.progressLabel2.resize(datas["progressNum"], 11)
        self.progressShow.move(datas["progressNum"] + 5, 167)
        self.nowFilesShow.setText(datas["path"])

    # 获取根目录下所有文件
    def traverseDir_mamb(self, paths):
        if not os.path.exists(paths):
            return [], 0
        resList = []
        ALLFIILESIZE = 0

        def inner(paths):
            nonlocal resList, ALLFIILESIZE
            filesList = os.listdir(paths)
            for filename in filesList:
                absPath = os.path.join(paths, filename)
                # 是否子目录
                if os.path.isdir(absPath):
                    inner(absPath)  # 递归循环子目录
                else:
                    absPath = absPath.replace("\\", "/")
                    resList.append({
                        "relativepath": absPath[2:],
                        "localpath": absPath
                    })
                    ALLFIILESIZE += os.path.getsize(absPath)

        inner(paths)
        return resList, ALLFIILESIZE

    # 选取文件夹上传
    def checkDir(self):
        try:
            if not self.downTh.is_alive() and not self.uploadTh.is_alive():
                FileDirectory = QFileDialog.getExistingDirectory(self, "选择目录")  # 选择目录，返回选中的路径
                if FileDirectory != "":
                    print("开始上传文件")
                    self.allfiles, self.ALLFIILESIZE = self.traverseDir_mamb(FileDirectory)
                    self.uploadTh = threading.Thread(target=self.UploadsStart, args=(self.allfiles, self.ALLFIILESIZE,))
                    self.uploadTh.start()
                    self.nowModeShow.setText("当前模式：上传")
        except:
            traceback.print_exc()

    # 下载按钮
    def down(self):
        try:
            if not self.downTh.is_alive() and not self.uploadTh.is_alive():
                print("开始下载刚才上传的文件")
                self.downTh = threading.Thread(target=self.DownloadStart, args=(self.allfiles, self.ALLFIILESIZE,))
                self.downTh.start()
                self.nowModeShow.setText("当前模式：下载")
        except:
            traceback.print_exc()

    # 总字节转换为大小
    def convert(self, bit):
        try:
            # B
            if bit < 1024:
                return str(bit) + "B"
            # KB
            elif 1024 <= bit < 2 ** 20:
                return str('%.2f' % (bit / (2 ** 10))) + "KB"
            # MB
            elif 2 ** 20 <= bit < 2 ** 30:
                return str('%.2f' % (bit / (2 ** 20))) + "MB"
            # GB
            elif 2 ** 30 <= bit < 2 ** 40:
                return str('%.2f' % (bit / (2 ** 30))) + "GB"
            # TB
            elif 2 ** 40 <= bit < 2 ** 50:
                return str('%.2f' % (bit / (2 ** 40))) + "TB"
            else:
                return "未知"
        except:
            return "未知"

    # 下载文件
    def DownloadStart(self, AllLocalFilesDownload, ALLFIILESIZE):
        try:
            client = socket.socket()
            ip_port = ("127.0.0.1", 5566)
            client.connect(ip_port)
            temp = "downFL".encode("utf-8")
            client.send(struct.pack("q", len(temp)))
            client.send(temp)
        except:
            traceback.print_exc()
            return

        try:
            begin = time.clock()
            speed = 0
            OKSIZE = 0
            for i in AllLocalFilesDownload:
                i["localpath"] = os.path.join(os.path.dirname(i["localpath"]), "副本/" + os.path.basename(i["localpath"])).replace("\\", "/")
                client.send(b"gon")  # 继续循环
                temp = (i['relativepath']).encode("utf-8")
                client.send(struct.pack("q", len(temp)))
                client.send(temp)  # 文件的完整相对路径

                file_size = client.recv(8)  # 接收文件大小
                file_size = struct.unpack("q", file_size)[0]

                filPath = os.path.dirname(i["localpath"])  # 除去文件名的路径
                try:
                    if not os.path.isdir(filPath):  # 判断路径是否存在，不存在则建立此路径
                        os.makedirs(filPath)
                except:
                    pass

                if file_size == 0:  # 源文件大小为零
                    with open(i["localpath"], "wb"):
                        pass
                    continue


                received_size = 0  # 当前已接收大小
                flagNum = 1024
                with open(i["localpath"], "wb") as f:
                    while True:
                        Rsize = file_size - received_size
                        if Rsize == 0:
                            break
                        elif Rsize > flagNum:
                            Rsize = flagNum
                        dataTemp = client.recv(Rsize)
                        received_size += len(dataTemp)
                        speed += len(dataTemp)
                        OKSIZE += len(dataTemp)
                        f.write(dataTemp)

                        interval = time.clock() - begin  # 从begin开始计算过了多少时间
                        if interval >= 0.5:
                            f.flush()
                            pronum = int(OKSIZE / ALLFIILESIZE * 100)
                            self.sigUpdateSpeed.emit({
                                "speed": self.convert(speed * 2) + "/s",
                                "progress": str(pronum) + "%",
                                "progressNum": int(450 * pronum / 100),
                                "path": i["localpath"]
                            })
                            begin = time.clock()  # 更新begin值
                            speed = 0
                        del dataTemp

                client.send(b"123456789")

            client.send(b"end")  # 发送结束信号
            client.close()
            del client
            print("下载完毕")
            self.sigUpdateSpeed.emit({
                "speed": "0/s",
                "progress": "100%",
                "progressNum": 450,
                "path": ""
            })

        except:
            del client
            traceback.print_exc()

        gc.collect()

    # 上传文件
    def UploadsStart(self, AllLocalFilesUpload, ALLFIILESIZE):
        try:
            client = socket.socket()
            ip_port = ("127.0.0.1", 5566)
            client.connect(ip_port)
            temp = "upload2".encode("utf-8")
            client.send(struct.pack("q", len(temp)))
            client.send(temp)
        except:
            traceback.print_exc()
            return
        try:
            begin = time.clock()
            speed = 0
            OKSIZE = 0
            for i in AllLocalFilesUpload:
                if os.path.exists(i["localpath"]):
                    client.send(b"gon")

                    temp = (i['relativepath']).encode("utf-8")
                    client.send(struct.pack("q", len(temp)))
                    client.send(temp)  # 文件的完整相对路径

                    file_size = os.stat(i["localpath"]).st_size
                    client.send(struct.pack("q", file_size))  # 打包发送文件总大小

                    flagNum = 1024
                    received_size = 0  # 当前已接收大小
                    with open(i["localpath"], "rb") as f:
                        while True:
                            Rsize = file_size - received_size
                            if Rsize == 0:
                                break
                            elif Rsize > flagNum:
                                Rsize = flagNum
                            dataTemp = f.read(Rsize)
                            received_size += len(dataTemp)
                            client.send(dataTemp)
                            OKSIZE += len(dataTemp)
                            speed += len(dataTemp)
                            interval = time.clock() - begin  # 从begin开始计算过了多少时间
                            if interval >= 0.5:  # 大于一秒
                                pronum = int(OKSIZE / ALLFIILESIZE * 100)
                                self.sigUpdateSpeed.emit({
                                    "speed": self.convert(speed*2) + "/s",
                                    "progress": str(pronum) + "%",
                                    "progressNum": int(450 * pronum / 100),
                                    "path": i["localpath"]
                                })
                                begin = time.clock()  # 更新begin值
                                speed = 0
                            del dataTemp


                    client.send(b"123456789")


            client.send(b"end")
            client.close()
            del client
            print("上传完成")
            self.sigUpdateSpeed.emit({
                "speed": "0/s",
                "progress": "100%",
                "progressNum": 450,
                "path": ""
            })

        except:
            del client
            gc.collect()
            traceback.print_exc()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = fileTransfers()
    sys.exit(app.exec_())




