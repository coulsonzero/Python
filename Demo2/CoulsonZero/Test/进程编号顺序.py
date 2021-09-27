from multiprocessing import Process
import os

def func(name, ages):
    print('当前进程ID:', os.getpid())
    print('父进程ID:', os.getppid())


if __name__=='__main__':
    print('主进程ID:', os.getpid())
    p=Process(target=func, args=('coulson', 23))
    #p=Process.(targe=func, kwargs={23, 'name': 'coulson')
    p.start()
