import os, time, sys,tkinter
import pyautogui as pg
from tkinter import * 
from tkinter.messagebox import * 

#登录界面
class login_GUI(object):
   def __init__(self):
      self.frame = Tk()        
      self.frame.title("QuickSend Helper")
      self.frame.geometry("400x180+400+100")               
      self.Label_username = Label(self.frame, text="User             ", font=("Verdana",12))
      self.Label_username.place(x=20,y=20)       
      self.Entry_username = Entry(self.frame, font=("Consola",14))       
      self.Entry_username.place(x=130,y=20)    
      self.Label_password = Label(self.frame, text="Password         ", font=("Verdana",12))   
      self.Label_password.place(x=20,y=70)        
      self.Entry_password = Entry(self.frame, font=("Consola",14),show='*')        
      self.Entry_password.place(x=130,y=70)
      
      self.Button_login = Button(self.frame, text="Log in", width=8, font=("Verdana",10),command = self.login)       
      self.Button_login.place(x=250,y=120)       
      self.Button_cancer = Button(self.frame, text="Cancel", width=8, font=("Verdana",10),command = self.cancer)       
      self.Button_cancer.place(x=130,y=120)          
      self.password_error_times = 0        
      self.is_disable = False    
   def run(self):        
      self.frame.mainloop()

      
   def login(self):              
      username = str(self.Entry_username.get())    
      password = str(self.Entry_password.get())
      if username.strip().lower() != "coulson":            
         showinfo("系统消息","用户名不存在，请核实后再登录！")        
      elif password.strip() != "abc1":            
         self.password_error_times += 1                       
         if self.password_error_times >= 3:                
            self.is_disable = True                       
            if self.is_disable:                
               showinfo("系统消息","密码输入错误已达三次，账号已锁定，请联系管理员")            
         else:                
            showinfo("系统消息", "密码错误！")        
      else:            
            #showinfo("系统消息","登录成功")
            self.password_error_times = 0
            self.frame.destroy()

            tkinter.Tk().withdraw()  #出现两个弹窗解决方法 
            showinfo("QuickSend helper使用说明", '''
         一.使用前检查：
            1. 管理员权限运行
            2. 弹出U盘
            3. 将需要执行的文件夹放入桌面文件夹"#quciksend"内
            4. 命名规则：
                  1q  ==========>> 9q 
                  1q副本(0) ===>>  1q副本(9)
            5.将其他窗口隐藏"最小化"
            
         请务必检查以免影响识别!!!
              
            二.影响识别成功率的因素
            A.网络延迟
            B.身份弹窗
            C.鼠标点击位置错误（检查U盘、#quicksend中的子文件夹）

            ps: 鼠标移动至屏幕左上角几秒可停止运行程序
                运行结束反馈命令窗口停留60min后自动关闭

            ———————————CoulsonZero——————————
            ''' )










            
            



            
   def cancer(self):        
   # 实现窗体的关闭        
      self.frame.destroy()  #退出窗口
      time.sleep(3)
      sys.exit()  #退出程序

      
      
if __name__ == '__main__':
   this_login = login_GUI()    
   this_login.run()
   
