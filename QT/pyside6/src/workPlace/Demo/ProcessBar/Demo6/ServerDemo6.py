"""
@author: coulson
@version: 2021/7/23  14:26
"""
# tcp_big_file_server.py
import socket
import os
import json
import time

server = socket.socket()    # 默认就是tcp
server.bind(('127.0.0.1', 8000))
server.listen()

print('服务启动...')
while True:
    conn, addr = server.accept()
    print('新的客户端：', addr)
    while True:
        try:
            data = conn.recv(2048)
            dic = json.loads(data.decode())
            if dic.get('option') == '1':
                base_path = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(base_path,dic.get('name'))
                conn.send('ok'.encode())    # 告诉客户端，准备好接收文件了
                # 准备接收发来的文件内容
                with open(file_path, 'ab') as f:
                    while dic['file_size']:
                        content = conn.recv(1024)
                        f.write(content)
                        dic['file_size'] -= len(content)
            print('有连接出现异常断开：', str(e))
        except Exception as e:
            break
    conn.close()
server.close()
