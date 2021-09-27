from tkinter import *
#import tkinter as tk
from tkinter import ttk,messagebox


'''先写个登录框框吧，直接上函数吧，类真的累'''


def login(master):
    login_frame = Frame(master)
    login_frame.grid(padx=15, pady=15)

    ttk.Label(login_frame, text='用户名').grid(column=1, row=1, columnspan=2)
    ttk.Entry(login_frame, ).grid(column=3, row=1, columnspan=3)

    ttk.Label(login_frame, text='密码').grid(column=1, row=2, columnspan=2)
    ttk.Entry(login_frame, show='*').grid(column=3, row=2, columnspan=3)

    def reg():
        '''这里就写你的登录需要的内容就行'''
        reg_top = Toplevel(login_frame)
        Label(reg_top, text='用户注册').grid(column=2, row=2)

    def cert():
        '''这里需要验证用户名和密码对不对，不对就蹦出个对话框告诉他，对就destroy'''
        login_frame.destroy()  # 我这里为了测试直接销毁了

    ttk.Button(login_frame, text='注册', command=reg).grid(column=2, row=3, columnspan=2, pady=15)
    ttk.Button(login_frame, text='登录', command=cert).grid(column=4, row=3, pady=15)

    return login_frame  # 这里一定要return啊
'''下面就是用户登录成功了应该出现的页面'''
def MainPage(master):
    window =Frame(master)
    window.grid()
    text=Text(window)
    text.grid()
    text.insert('end','没错你登录成功，所以看到了我')

if __name__ == "__main__":
    my_window = Tk()
    login = login(my_window)
    try:#因为用户可能直接关闭主窗口，所以我们要捕捉这个错误
        my_window.wait_window(window=login)#等待直到login销毁，不销毁后面的语句就不执行
        MainPage(my_window)
    except:
        pass
    my_window.mainloop()
