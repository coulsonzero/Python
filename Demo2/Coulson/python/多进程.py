# 多进程实现并发
from multiprocessing import Process
import time

#唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(0.5)
        #跳舞
def dance():
    for i in range(4):
        print("跳舞...")
        time.sleep(0.7)

if __name__ == '__main__':
    #单进程
    #sing()
    #dance()
    # 多进程
    sing_process = Process(target=sing)
    dance_process = Process(target=dance)
    sing_process.start()
    dance_process.start()