
#1.导入进程包
from multiprocessing import Process
def func():
    pass
if __name__=='__main__':

    # 2.创建子进程并指定执行的任务
    # targe: 指定进程执行的函数名
    # args：指定元组方式给指定任务传递参数
    # kwargs：使用字典方式给指定任务传参
    func_p= Process(target=func)#, args=(name, ages, ...)
    #3. 启动子进程
    func_p.start()
    #等待执行结束
    func_p.join()