"""
@author: coulson
@version: 2021/7/23  14:15
"""
import socket
import os
import json

def file_put(filedir):

    client = socket.socket()
    client.connect(('127.0.0.1', 8000))
    print('socket服务正在运行...')
    if os.path.isfile(filedir):
        print('the file path is {}'.format(filedir))
        file_name = filedir
        file_size = os.stat(file_name).st_size
        file_msg = {"action": "put", "name": file_name, "size": file_size}
        client.send(bytes(json.dumps(file_msg), encoding="utf-8"))          #发送传输需要的数据
        print("文件名: %s --> 文件大小: %s " % (file_name,file_size))
        with open(file_name, "rb") as f:
            for line in f:
                client.send(line)  #开始发送数据
                print("文件已发送: %s" % len(line))
            print("文件发送完成...")
    else:
        print('please check your file path,the file path {} is not exist'.format(file_path))
if __name__ == '__main__':
    for i in range(1,3):
       out_emb_path='/home/z/Documents/face_detect_yolov4_yolov4tiny_ssd-master/tools/yoloface_hkcamera{}_arcface_feature.pkl'.format(i)
       print(out_emb_path)
       file_put(out_emb_path)        #调用函数,传输文件
