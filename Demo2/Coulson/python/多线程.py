import threading
import time
def sing(num, name):
    for i in range(num):
        print(name,":唱歌.")
        time.sleep(0.5)

def dance(count):
    for i in range(count):
        print("跳舞")
        time.sleep(0.7)
if __name__ ==  '__main__':
    #args:以元组的方式给执行任务传递参数
    sing_thread=threading.Thread(target=sing,args=(3,"xiaoming"))
    # kwargs:以字典方式给执行任务传递参数
    dance_thread=threading.Thread(target=dance, kwargs={"count": 4})
    sing_thread. start()
    dance_thread. start()
