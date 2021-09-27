"""
@author: coulson
@version: 2021/7/23  14:26
"""
# tcp_big_file_client.py
import socket
import os
import json
import time


def print_bar1(percent):
    bar = '\r' + '*' * int((percent * 100)) + ' %3.0f%%|' % (percent*100) + '100%'
    print(bar, end='', flush=True)




def main(fp):
    client = socket.socket()
    client.connect(('127.0.0.1', 8000))
    while True:
        file_path = fp.text()   #input('请输入要上传文件的绝对路径：')
        print(file_path)
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        dic = {"option": "1", "name": file_name, "file_size": file_size}
        client.send(json.dumps(dic).encode())
        msg = client.recv(100) # 判断服务端准备好接收文件了，还可以防止粘包
        begin_size = file_size
        if msg.decode() == 'ok':
            # 服务端表示准备好接收文件了，开始循环发送文件
            with open(file_path, 'rb') as f:
                while file_size:
                    content = f.read(1024)
                    client.send(content)
                    file_size -= len(content)
                    print_bar1(round((begin_size - file_size) / begin_size, 2))
                print('')
            break
    client.close()

if __name__ == '__main__':

    main()