from tkinter import *
import tkinter as tk
from tkinter import filedialog, dialog
import os

success= []

window = Tk()
window.title('窗口标题')  # 标题
window.geometry('500x500')  # 窗口尺寸

file_path = ''

file_text = ''

text1 = Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()


var_X=IntVar()
Entry_X = Entry(window,font=('consolas',14),width=9,textvariable=var_X)
Entry_X.pack()
var_X.set('')
Entry_X.insert(0,800)

var_Y=IntVar()
Entry_Y = Entry(window,font=('consolas',14),width=9,textvariable=var_Y)
Entry_Y.pack()
var_Y.set('')
Entry_Y.insert(0,900)

S1 = Entry_X.get()
S2 = Entry_Y.get()


def open_file():
    '''
    打开文件
    :return:
    '''
    global file_path
    global file_text
    file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(r'C:\Users\21059\Desktop\#quicksend')))
    print('打开文件：', file_path)
    if file_path is not None:

        with open(file=file_path, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
        #text1.insert('insert', file_text)
        Entry_X.delete(0, END)
        Entry_X.insert('insert', 400)
        Entry_Y.delete(0, END)
        Entry_Y.insert('insert', 400)

def save_file():
    global file_path
    global file_text
    file_path = filedialog.asksaveasfilename(title=u'保存文件',initialdir=(os.path.expanduser(r'C:\Users\21059\Desktop\#quicksend\code')))
    print('保存文件：', file_path)


    #file_text = text1.get('1.0', END)
    #file_text=Entry_X.get()
    success=[]
    success.append(200)
    success.append(500)


    if file_path is not None:
        with open(file=file_path, mode='a+', encoding='utf-8') as file:
            file.write(S1)
            file.write(S2)
        #text1.delete('1.0', END)
        #Entry_X.delete('1.0', END)
        dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
                             'strings': ('OK', 'Cancle')})
        print('保存完成')



menubar= Menu(window)
filemenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label='QuickSend',menu=filemenu)
filemenu.add_command(label='run')
filemenu.add_command(label='open',command=open_file)
filemenu.add_command(label='save',command=save_file)
filemenu.add_separator()
filemenu.add_command(label='exit', command=window.quit)

aboutmenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label='Help', menu= aboutmenu)
aboutmenu.add_command(label='使用指南')
aboutmenu.add_command(label='about')


window.config(menu=menubar)



window.mainloop()