import tkinter as tk
import tkinter.scrolledtext as tst

root = tk.Tk()
root.title('文本编辑器')
# v = tk.StringVar()
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.createMenu()
        root['menu'] = self.menubar
        root.bind('<Button-3>', self.f_popup)
        # root.bind('<Button-1>', self.callback)

        # 状态栏
        self.status = tk.StringVar()
        self.status.set('Ln: 1 Col: 1')
        self.lblStatus = tk.Label(self, textvariable=self.status, anchor='c')
        self.lblStatus.grid(row=7, column=0, columnspan=20, sticky=tk.S + tk.E)
        root.bind('<Key>', self.loc)
        root.bind('<Button-1>', self.loc)

    def createWidgets(self):
        self.textEdit = tst.ScrolledText(self, width=80, height=25)
        self.textEdit.grid(row=0, column=0, rowspan=6)

        '''
        self.lblState = tk.Label(self, text="状态栏:")
        self.lblState.grid(row=7, column=0, columnspan=10)
        self.entryState = tk.Entry(self, textvariable=v)
        self.lblState.grid(row=7, column=11, columnspan=20)
        '''

    def createMenu(self):
        self.menubar = tk.Menu(root)
        # 创建子菜单
        self.menufile = tk.Menu(self.menubar)
        self.menuedit = tk.Menu(self.menubar, tearoff=0)
        self.menuhelp = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.menufile)
        self.menubar.add_cascade(label="Edit", menu=self.menuedit)
        self.menubar.add_cascade(label="Help", menu=self.menuhelp)

        # 添加菜单项
        self.menufile.add_command(label='New', command=self.f_new)
        self.menufile.bind("<Control-N>", self.f_new)
        self.menufile.add_command(label='Open', command=self.f_open)
        self.menufile.bind("<Control-O>", self.f_open)
        self.menufile.add_command(label='Save', accelerator='^A',
                                  command=self.f_save)
        self.menufile.bind("<Control-S>", self.f_save)
        # 分隔
        self.menufile.add_separator()
        self.menufile.add_command(label='Exit', command=root.destroy)
        self.menuedit.add_command(label="Cut", command=self.f_cut, accelerator='Ctrl+T')
        self.menuedit.bind("<Control-T>", self.f_cut)
        self.menuedit.add_command(label="Copy", command=self.f_copy, accelerator='Ctrl+C')
        self.menuedit.bind("<Control-T>", self.f_copy)
        self.menuedit.add_command(label="Paste", command=self.f_paste, accelerator='Ctrl+V')
        self.menuedit.bind("<Control-T>", self.f_paste)
        self.menuedit.add_command(label="Delete", command=self.f_delete, accelerator='Ctrl+D')
        self.menuedit.bind("<Control-T>", self.f_delete)
        self.menuhelp.add_command(label="About", command=self.f_about)

    def f_new(self):
        root.title('untitle')  # 新建文件title
        self.textEdit.delete(1.0, tk.END)

    def f_open(self):
        self.textEdit.delete(1.0, tk.END)
        fname = tk.filedialog.askopenfilename(filetypes=[('Python源文件', '.py')])
        with open(fname, 'r', encoding='utf-8') as f1:
            str1 = f1.read()
        self.textEdit.insert(0.0, str1)

    def f_save(self):
        str1 = self.textEdit.get(1.0, tk.END)
        fname = tk.filedialog.asksaveasfilename(filetypes=[('Python源文件', '.py')])
        with open(fname, 'w', encoding='utf-8') as f1:  # 打开文件
            f1.write(str1)

    def f_about(self):
        tk.messagebox.showinfo('关于', '版本V 1.0.1')

    def f_cut(self):
        try:
            str1 = self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()
            self.textEdit.clipboard_append(str1)
            self.textEdit.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except:
            pass

    def f_copy(self):
        try:
            str1 = self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()
            self.textEdit.clipboard_append(str1)
        except:
            pass

    def f_paste(self):
        str1 = self.textEdit.selection_get(selection='CLIPBOARD')
        try:
            self.textEdit.replace(tk.SEL_FIRST, tk.SEL_LAST, str1)
        except:
            self.textEdit.insert(tk.INSERT, str1)

    def f_delete(self):
        try:
            str1 = self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except:
            pass
        # 定位光标位置，缺点读字符串的位置。。，不知道换行在哪里，仍需加强条件调试。

    def loc(self, event=None):
        s = str(self.textEdit.index('insert')).split('.')
        statusXY = 'Ln: ' + str(s[0]) + 'Col: ' + str(s[1])
        self.status.set(statusXY)

    def f_popup(self, event):
        self.menuedit.post(event.x_root, event.y_root)


app = Application(master=root)
app.mainloop()
root.mainloop()
