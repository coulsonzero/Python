import socket
import os
import struct
import sys
import threading
import time
import traceback
import gc


class fileserverclass:
    server = socket.socket()
    LocalPath = "C:/test/fileBases"

    def __init__(self):
        self.server.bind(("0.0.0.0", 5566))  # 绑定监听端口
        self.server.listen(10)  # 监听

    def __dir__(self):
        os._exit(0)

    # 连接处理线程
    def __run(self, conn, addr):
        try:
            Size = conn.recv(8)
            Size = struct.unpack("q", Size)[0]
            option = conn.recv(Size).decode("utf-8")
            print(option)
            if option == "downFL":
                try:
                    while True:
                        step = conn.recv(3)
                        if step == b"end":
                            break
                        elif step == b"get":  # 结束本次循环开始下一循环
                            continue
                        elif step == b"gon":
                            Size = conn.recv(8)
                            Size = struct.unpack("q", Size)[0]
                            filename = conn.recv(Size).decode("utf-8")  # 文件的完整相对路径
                            filename = self.LocalPath + filename

                            file_size = os.stat(filename).st_size  # 获取文件大小
                            conn.send(struct.pack("q", file_size))  # 打包发送文件总大小

                            flagNum = 1024
                            received_size = 0  # 当前已接收大小
                            with open(filename, "rb") as f:
                                while True:
                                    Rsize = file_size - received_size
                                    if Rsize == 0:
                                        break
                                    elif Rsize > flagNum:
                                        Rsize = flagNum
                                    dataTemp = f.read(Rsize)
                                    received_size += len(dataTemp)
                                    conn.send(dataTemp)
                                    del dataTemp
                            conn.recv(9)  # 下载完毕

                    conn.close()
                    del conn
                    gc.collect()  # 释放内存
                except:
                    conn.close()
                    del conn
                    gc.collect()  # 释放内存
                    print("下载 - 出错:")
                    print("\n\n" + time.strftime("%Y-%m-%d   %H:%M:%S", time.localtime()))
                    traceback.print_exc()
                    sys.stdout.flush()

            elif option == "upload2":
                try:
                    while True:
                        step = conn.recv(3)
                        if step == b"end":
                            break
                        elif step == b"get":
                            continue
                        elif step == b"gon":
                            Size = conn.recv(8)
                            Size = struct.unpack("q", Size)[0]
                            relativepath = conn.recv(Size).decode("utf-8")  # 文件的完整相对路径

                            Size = conn.recv(8)
                            file_size = struct.unpack("q", Size)[0]  # 获取文件总大小

                            filename = self.LocalPath + relativepath
                            filPath = os.path.dirname(filename)  # 除去文件名的路径
                            if not os.path.isdir(filPath):  # 判断路径是否存在，不存在则建立此路径
                                try:
                                    os.makedirs(filPath)
                                except:
                                    pass

                            if file_size == 0:  # 源文件大小为零
                                with open(filename, "wb"):
                                    pass
                                continue

                            gc.collect()
                            flagNum = 1024
                            received_size = 0
                            with open(filename, "wb") as f:
                                while True:
                                    Rsize = file_size - received_size
                                    if Rsize == 0:
                                        break
                                    elif Rsize > flagNum:
                                        Rsize = flagNum
                                    dataTemp = conn.recv(Rsize)
                                    received_size += len(dataTemp)
                                    f.write(dataTemp)
                            conn.send(b"123465789")

                    conn.close()
                    del conn
                    gc.collect()  # 释放内存
                except:
                    conn.close()
                    del conn
                    gc.collect()  # 释放内存
                    print("上传 - 出错:")
                    print("\n\n" + time.strftime("%Y-%m-%d   %H:%M:%S", time.localtime()))
                    traceback.print_exc()
                    sys.stdout.flush()

        except:
            try:
                conn.close()
            except:
                pass
            del conn, addr
            gc.collect()


    def do(self):
        print("服务器开启")
        while True:
            conn, addr = self.server.accept()  # 等待连接
            print(conn, addr)
            tempTh = threading.Thread(target=self.__run, args=(conn, addr,))
            tempTh.start()




if __name__ == "__main__":
    test = fileserverclass()
    test.do()

