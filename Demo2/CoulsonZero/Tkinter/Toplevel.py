from tkinter import *
import os, time, sys,tkinter
import pyautogui as pg
from tkinter import *
from tkinter.messagebox import *


window = Tk()
window.title('QuickSend.py Helper')
window.geometry('800x400+300+100')
window.iconphoto(True, PhotoImage(file=r'C:\Users\21059\Desktop\#quicksend\code\black.png'))

#Data--Entry
Label_data = Label(window,text="Enter folder data",font=('微软雅黑',10))
Label_data.pack()  #column=0, row=0, sticky='W'
var_data=StringVar()
Entry_data = Entry(window,font=('consolas',14),width=20,textvariable=var_data)
var_data.set('')
Entry_data.insert(0,"3.29")
Entry_data.pack() #column=0, row=1, sticky='W'
def Login_Helper():
    class login_GUI(object):
        def __init__(self):
            self.frame = Toplevel()
            #self.frame.attributes('-alpha',0.5)    #是窗口透明度50%
            self.frame.attributes("-topmost", True)
            self.frame.title("Log in")
            self.frame.geometry("400x180+500+100")
            window.iconify()

            self.Label_username = Label(self.frame, text="User             ", font=("Verdana", 12))
            self.Label_username.place(x=20, y=20)
            self.Entry_username = Entry(self.frame, font=("Consola", 14))
            self.Entry_username.place(x=130, y=20)
            self.Label_password = Label(self.frame, text="Password         ", font=("Verdana", 12))
            self.Label_password.place(x=20, y=70)
            self.Entry_password = Entry(self.frame, font=("Consola", 14), show='*')
            self.Entry_password.place(x=130, y=70)

            self.Button_login = Button(self.frame, text="Log in", width=8, font=("Verdana", 10), command=self.login)
            self.Button_login.place(x=250, y=120)
            self.Button_cancer = Button(self.frame, text="Cancel", width=8, font=("Verdana", 10), command=self.cancer)
            self.Button_cancer.place(x=130, y=120)
            self.password_error_times = 0
            self.is_disable = False



        def run(self):
            self.frame.mainloop()

        def login(self):
            username = str(self.Entry_username.get())
            password = str(self.Entry_password.get())
            if username.strip().lower() != "coulson":
                showinfo("系统消息", "用户名不存在，请核实后再登录！")
            elif password.strip() != "abc1":
                self.password_error_times += 1
                if self.password_error_times >= 3:
                    self.is_disable = True
                    if self.is_disable:
                        showinfo("系统消息", "密码输入错误已达三次，账号已锁定，请联系管理员")
                else:
                    showinfo("系统消息", "密码错误！")
            else:
                # showinfo("系统消息","登录成功")
                self.password_error_times = 0
                self.frame.destroy()
                #Tk().withdraw()  # 出现两个弹窗解决方法
                window.deiconify()
                return True
                #window.mainloop()

                #Tk().withdraw()  # 出现两个弹窗解决方法

        def cancer(self):
            # 实现窗体的关闭
            self.frame.destroy()  # 退出窗口
            time.sleep(3)
            sys.exit()  # 退出程序

    if __name__ == '__main__':
        this_login = login_GUI()
        this_login.run()
Button_run = Button(window,text='Log in',bg='pink',font=('Arial',12),width=10,height=2,command=Login_Helper)   #文本小写！！
Button_run.pack(anchor=NE)

#Login_Helper()
Button_run = Button(window,text='运行',bg='pink',font=('Verdana',15),width=15,height=2,activebackground='white',bd=2)   #文本小写！！command=run_Helper
Button_run.pack()
#mainloop()
window.mainloop()

