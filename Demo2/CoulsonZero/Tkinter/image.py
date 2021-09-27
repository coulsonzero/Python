import tkinter as tk

root = tk.Tk()

# 增加背景图片
photo = tk.PhotoImage(file=r"C:\\Users\21059\\Desktop\\3.png")
theLabel = tk.Label(root,
                    text = "我是内容,\n请你阅读",
                    justify = tk.LEFT,   #对其方式
                    image = photo,
                    compound = tk.CENTER, #关键：设置为背景图片
                    font = ("华文行楷", 20),
                    fg = "white")  # 前景色
theLabel.pack()

tk.mainloop()
