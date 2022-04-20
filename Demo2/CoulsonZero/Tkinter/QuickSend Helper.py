import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import *
import os, time, sys, tkinter
import pyautogui as pg
from tkinter.messagebox import *
from tkinter import filedialog, dialog

window=tk.Tk()
window.title('QuickSend.py Helper')
window.geometry('800x400+300+100')
window.iconphoto(True, PhotoImage(file=r'C:\Users\21059\Desktop\#quicksend\code\black.png'))
window.resizable(False,False)

#滚动条
yscrollbar=Scrollbar()
yscrollbar.pack(side=LEFT,fill=Y)
#PanedWindow
m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
m1.pack(side=LEFT)  #fill=BOTH, expand=1
left = Text(window)
m1.add(left)
m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
m1.add(m2)
#链接
yscrollbar.config(command=left.yview)
left.config(yscrollcommand=yscrollbar.set)

#left.insert(END,func)
#left.delete(1.0,END)
#文本
#text_print=Text(window)
#text_print.pack(side=LEFT)

#yscrollbar.config(command=text_print.yview)
#text_print.config(yscrollcommand=yscrollbar.set)

#text_print.insert(END,func)
#ttk.Frame
tabControl = ttk.Notebook(window)
tab1 = Frame(tabControl)
tabControl.add(tab1, text='文件配置')
tab2 = Frame(tabControl)
tabControl.add(tab2, text='一般设置')
tab3 = Frame(tabControl)
tabControl.add(tab3, text='环境Ⅰ')
tab4 = Frame(tabControl)
tabControl.add(tab4, text='环境 Ⅱ')
tabControl.pack(expand=1, fill='both')

#LabelFrame tab1
setup1 = LabelFrame(tab1, text=' Setup ', fg='red')
setup1.grid()  #column=0, row=0, padx=8, pady=4

#Data--Entry
Label_data = Label(setup1,text="Enter folder data",font=('微软雅黑',10))
Label_data.grid()  #column=0, row=0, sticky='W'
var_data=StringVar()
Entry_data = Entry(setup1,font=('consolas',14),width=20,textvariable=var_data)
var_data.set('')
Entry_data.insert(0,"3.29")
Entry_data.grid() #column=0, row=1, sticky='W'


#文件夹数量--Scroll
Label_foldernums= Label(setup1,fg='#FF00FF', text='')
Label_foldernums.grid()
def print_foldernums(v):
    Label_foldernums.config(text=v+'q-data')
var_fnums=IntVar()
Scale_foldernums = Scale(setup1,from_=0,to=9,orient=HORIZONTAL,
                         length=200,width=15,resolution=1,
                         tickinterval=3,repeatdelay=100,
                         variable=var_fnums,command=print_foldernums)
Scale_foldernums.set(4)
Scale_foldernums.grid()
Scale_foldernums.bind('<<ScaleSelected>>',print_foldernums)

#副本数量---Scroll
def print_surfilenums(v):
    Label_surfilenums.config(text='nq - 副本 ('+ v +')')
var_snums=IntVar()
Scale_surfilenums = Scale(setup1,from_=0,to=9,orient=HORIZONTAL,
                          length=200,width=15,resolution=1,
                          tickinterval=3,repeatdelay=100,
                          variable=var_snums,command=print_surfilenums)
Scale_surfilenums.set(8)
Scale_surfilenums.grid()
Scale_surfilenums.bind('<<ScaleSelected>>',print_surfilenums)
Label_surfilenums= Label(setup1,fg='green', text='')
Label_surfilenums.grid()

#副本名称
#def print_surfoldername(event):
    #print(var_sname.get())
var_sname=StringVar()
com_surfoldername = ttk.Combobox(setup1, textvariable=var_sname,width=20) #,state='readonly'
com_surfoldername['value']=('q - 副本 ','q','q-')
com_surfoldername.grid()
com_surfoldername.current(0)
#com_surfoldername.bind('<<ComboboxSelected>>',print_surfoldername)

def run_Helper():
    data = Entry_data.get()         #日期
    folders_nums = var_fnums.get()
    t = var_snums.get()            #副本数量
    folder_name = var_sname.get()
    Entry_data.delete(0,'end')
    left.delete(1.0, END)
    string_info='    文件夹: '+str(folders_nums)+'q-'+str(data)+'\n'+'副本文件夹: '+str(t)+folder_name+'(0)'+'\n'
    #print(data,folders_nums,t,folder_name)
    left.insert(END, string_info)
    #left.insert(tk.INSERT, '\n')
    # left.delete(1.0,END)

#运行按钮
Button_run = Button(setup1,text='运行',bg='pink',font=('Verdana',15),
                    width=15,height=2,activebackground='white',bd=2,command=run_Helper)   #文本小写！！
Button_run.grid()

#LabelFrame tab2
setup2 = LabelFrame(tab2, text=' Setup2 ', fg='red')
setup2.grid()  #column=0, row=0, padx=8, pady=4

#PC
Label_pcrow= Label(setup2,fg='#FF00FF', text='')
Label_pcrow.grid()
def print_pcrow(pc):
    Label_pcrow.config(text='电脑在第'+pc+'行')
var_pr=IntVar()
Scale_pcrow = Scale(setup2,from_=1,to=11,orient=HORIZONTAL,
                    length=200,width=15,resolution=1,
                    tickinterval=5,repeatdelay=100,
                    variable=var_pr,command=print_pcrow)
Scale_pcrow.set(3)
Scale_pcrow.grid()
Scale_pcrow.bind('<<ScaleSelected>>',print_pcrow)


#'#quicksend'

def print_qrow(q):
    Label_qrow.config(text='#quicksend第'+q+'行')
var_qr=IntVar()
Scale_qrow = Scale(setup2,from_=1,to=11,orient=HORIZONTAL,
                   length=200,width=15,resolution=1,
                   tickinterval=5,repeatdelay=100,
                   variable=var_qr,command=print_qrow)
Scale_qrow.set(4)
Scale_qrow.grid()
Scale_qrow.bind('<<ScaleSelected>>',print_qrow)
Label_qrow= Label(setup2,fg='BLUE', text='')
Label_qrow.grid()

#   1q-data
def print_1q(v):
    Label_1q.config(text='#1q-data在第'+v+'行')
var_1q=IntVar()
Scale_1q = Scale(setup2,from_=1,to=11,orient=HORIZONTAL,
                length=200,width=15,resolution=1,
                tickinterval=5,repeatdelay=100,
                variable=var_1q,command=print_1q)
Scale_1q.set(5)
Scale_1q.grid()
Scale_1q.bind('<<ScaleSelected>>', print_1q)
Label_1q= Label(setup2,fg='red', text='')
Label_1q.grid()

#默认设置
def save_Q():
    D_row=int(var_pr.get())
    q_row = int(var_qr.get())
    q_data= int(var_1q.get())
    #print(D_row,q_row,m0_row)
save_Q()
Button_save_Q = Button(setup2,text='保存',font=('Arial',12),
                       width=22,height=3,activebackground='black',command=save_Q)   #文本小写！！
Button_save_Q.grid()

#LabelFrame tab3
setup3 = LabelFrame(tab3, text=' Setup3 ', fg='red')
setup3.grid()  #column=0, row=0, padx=8, pady=4

#X--Entry
Label_X = Label(setup3,text="X",font=('微软雅黑',10))
Label_X.grid(column=0, row=0, sticky='W')
var_X=StringVar()
Entry_X = Entry(setup3,font=('consolas',14),width=8,textvariable=var_X)
var_X.set('')
Entry_X.insert(0,800)

Entry_X.grid(column=1, row=0, sticky='W')

#Y--Entry
Label_Y = Label(setup3,text="Y",font=('微软雅黑',10))
Label_Y.grid(column=3, row=0, sticky='W')
var_Y=IntVar()
Entry_Y = Entry(setup3,font=('consolas',14),width=9,textvariable=var_Y)
var_Y.set('')
Entry_Y.insert(0, 392)
Entry_Y.grid(column=4, row=0, sticky='W')
#S_X--Entry
Label_SX = Label(setup3,text="X",font=('微软雅黑',10))
Label_SX.grid(column=0, row=1, sticky='W')
var_SX=IntVar()
Entry_SX = Entry(setup3,font=('consolas',14),width=8,textvariable=var_SX)
var_SX.set('')
Entry_SX.insert(0,1120)
Entry_SX.grid(column=1, row=1, sticky='W')

#S_Y--Entry
Label_SY = Label(setup3,text="Y",font=('微软雅黑',10))
Label_SY.grid(column=3, row=1, sticky='W')
var_SY=IntVar()
Entry_SY = Entry(setup3,font=('consolas',14),width=9,textvariable=var_SY)
var_SY.set('')
Entry_SY.insert(0, 607)
Entry_SY.grid(column=4, row=1, sticky='W')

def callback(event):
    left.delete(1.0,END)
    string_callback='('+str(event.x_root)+','+str(event.y_root)+')'+'\n'
    left.insert(END,string_callback)
    #left.insert(END,event.x_root)
    #left.insert(END,',')
    #left.insert(END,event.y_root)
Button_click=Button(setup3,text='获取位置',font=('Arial',12),width=10,height=2,activebackground='black')
Button_click.bind('<Motion>',callback)
Button_click.grid(column=4, row=3, sticky='W')

#默认设置
def save_XY():
    x = int(var_X.get())
    y = int(var_Y.get())
    s_x = int(var_SX.get())
    s_y = int(var_SY.get())
    #print(x,y,s_x,s_y)

save_XY()
Button_save_Q = Button(setup3,text='保存',font=('Arial',12),
                       width=10,height=2,activebackground='black', command=save_XY)   #文本小写！！
Button_save_Q.grid(column=4, row=5, sticky='S')

#LabelFrame tab4
setup4 = LabelFrame(tab4, text=' Setup4 ', fg='red')
setup4.grid()  #column=0, row=0, padx=8, pady=4

#副本（0）
def print_m0row(surf):
    Label_m0row.config(text='副本 (0)在第'+surf+'行')
var_m0r=IntVar()
Scale_m0row = Scale(setup4,from_=1,to=11,orient=HORIZONTAL,
                    length=200,width=15,resolution=1,
                    tickinterval=5,repeatdelay=100,
                    variable=var_m0r,command=print_m0row)
Scale_m0row.set(3)
Scale_m0row.grid()
Scale_m0row.bind('<<ScaleSelected>>',print_m0row)
Label_m0row= Label(setup4,fg='#00FF00', text='')
Label_m0row.grid()
#r_max
def print_rmax(v):
    Label_rmax.config(text='导航栏总共'+ v +'行')
var_rm=IntVar()
Scale_rmax = Scale(setup4,from_=9,to=11,orient=HORIZONTAL,
                   length=200,width=15,resolution=1,tickinterval=2,
                   repeatdelay=100,variable=var_rm,command=print_rmax)
Scale_rmax.set(11)
Scale_rmax.grid()
Scale_rmax.bind('<<ScaleSelected>>',print_rmax)
Label_rmax= Label(setup4,fg='blue', text='')
Label_rmax.grid()
#f
def print_f(v):
    Label_f.config(text='Windows 7 / 10')
var_f=IntVar()
Scale_f = Scale(setup4,from_=18,to=20,orient=HORIZONTAL,
                length=200,width=15,resolution=2,
                tickinterval=2,repeatdelay=100,
                variable=var_f,command=print_f)
Scale_f.set(20)
Scale_f.grid()
Scale_f.bind('<<ScaleSelected>>', print_f)
Label_f= Label(setup4,fg='green', text='')
Label_f.grid()

#默认设置
def save_win():
    r_max = int(var_rm.get())
    f = int(var_f.get())
    m0_row = int(var_m0r.get())
    #print(r_max,f)
save_win()
Button_save_Q = Button(setup4,text='保存',font=('Arial',12),
                       width=10,height=2,activebackground='black',command=save_win)
Button_save_Q.grid(column=0, row=7, sticky='S')

def user_guide():
    frame_guide=Frame(window)
    showinfo('QuickSend.py Helper','''
    一.使用前检查：
    1) 桌面创建“#quicksend”文件夹，并将“code”源文件夹放于其中
    2）将需要发送的文件夹重命名后放于“#quicksend”
           文件夹：1q-3.29    --------->>   9q-3.29    
        子文件夹：1q - 副本 (0)   --->>>    1q - 副本 (9)
    3) 管理员权限启动程序
    4）检查U盘是否弹出，核对QuickSend“选择配置”内的导航栏信息
    5）将多余的副本(>9)文件夹隐藏/移出
    以免影响识别!!!
    
    二.影响识别成功率及速率的因素
    A.网络延迟
    B.身份弹窗
    C.鼠标点击位置错误（检查U盘、  #quicksend中的子文件夹）

    ps: 鼠标移动至屏幕左上角几秒可停止运行程序
        运行结束反馈命令窗口停留60min后自动关闭

————————————CoulsonZero————————————
    ''')
    frame_guide.pack()
def exit_Helper():
    if messagebox.askokcancel('QuickSend.py Helper', '是否确定退出?'):
        window.destroy()
#菜单栏
menubar= Menu(window)
filemenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label='QuickSend.py',menu=filemenu)
filemenu.add_command(label='run',command=run_Helper)
filemenu.add_command(label='open')
filemenu.add_command(label='save')
filemenu.add_separator()
filemenu.add_command(label='exit', accelerator = 'Shift+F4',command=exit_Helper)

aboutmenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label='Help',menu= aboutmenu)
aboutmenu.add_command(label='使用指南',command=user_guide)
window.config(menu=menubar)
window.mainloop()