import os, time, sys
import pyautogui as pg

#使用注意，使用期限
time.sleep(1)
pg.alert(text='''
一.使用前检查：
1.管理员权限启动
2.弹出U盘
3.请将文件夹<*q-3.23>放入桌面文件夹"#quciksend"
4.请将"#quciksend"其他副本(>9)隐藏/移出
5.其他窗口隐藏"最小化"

以免影响识别!!!


二.影响识别成功率及速率的因素
A.网络延迟
B.身份弹窗
C.鼠标点击位置错误（检查U盘、#quicksend中的子文件夹）

ps: 鼠标移动至屏幕左上角几秒可停止运行程序
    运行结束反馈命令窗口停留60min后自动关闭

——————————————————————CoulsonZero——————————————————————
''',title='QuickSend通用版',button='我已详细检查')



def now():
   return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

s = '2021-04-07 15:59:59'
pg.alert(text=f'''
北京时间:  {now()}
     
使用期限:  {s}
''',title='QuickSend稳定版', button ='ok')
if now() > s:
   pg.alert(text=f"软件使用时限已到，无法正常使用，请及时与CoulsonZero联系处理" ,title='QuickSend稳定版', button ='退出')
   time.sleep(2)
   sys.exit()
else:
   pass
   #输入框         滑块      滑块
   #文件夹日期、文件夹数量、副本数量
data=pg.prompt(text='文件夹日期<3.23>：',title='QuickSend通用版',default='')
folders_nums=int(pg.prompt(text='待执行文件夹<?q-3.23>总数：',title='QuickSend通用版',default=''))
t=int(pg.prompt(text=('副本(?)：'),title='QuickSend通用版',default=''))
time.sleep(1)
#win7(r=18)
#为方便计算设定
#q=D+1,n_1=q+1=D+2,只要知道电脑行数，就知道#quicksend与1q-date行数
#n从1开始计数，m从0开始计数，


#输入框3个，滑条1个                                     滑条         滑条                 滑条                          下行选择框                                   
#行距、2个坐标点、最大行、（默认一般不改，换电脑改）||||此电脑位置、#quicksend文件夹位置、副本(0)位置（每次需要再改）|||||副本名称（每次登录后设置）
folder_name='q - 副本 '
f=20  #(win7 --> f=18)
c=20
x,y,s_x,s_y=800,392,1120,607
D_row=3
q_row=4
m0_row=3
r_max=11

#q_row=D_row+1
#m_row=m0_row+m
#q1_row=q_row+1=D_row+2
#n_max=r_max-q_row=r_max-(D_row+1)   #n_max<=9
#m_max=r_max-m0_row          #m_max<=9

 

time.sleep(2)
for n in range(1, folders_nums+1):
   for m in range(0,int(t)+1):
      os.startfile(r'C:\Users\Administrator\Desktop\#quicksend\{}q-{}\{}{}({})\QuickSend.exe'.format(n,data,n,folder_name,m))
      time.sleep(1)
      #身份弹窗
      select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\select.png', grayscale=False, confidence=0.6)
      time.sleep(0.5)
      abnormal = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\abnormal2.png', grayscale=False, confidence=0.6)
      time.sleep(0.5)
      if select == None:
         if abnormal != None:
            confirm = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\confirm.png', grayscale=False, confidence=0.6)
            time.sleep(1)
            pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\confirm.png', grayscale=False, confidence=0.6),duration=0.4)
            time.sleep(2)
         else:
            time.sleep(2)
            break
      else:
         pass
      pg.click(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\select.png', grayscale=False, confidence=0.6),duration=0.4)
      pg.press('enter')
      time.sleep(0.3)
      #参数设置
      #第一列
      #电脑   y+(D_row-1)f
      pg.click(x,y+(D_row-1)*f,duration=0.4)
      #quicksend  y+(q_row-1)*f
      pg.click(x,y+(q_row-1)*f,duration=0.4)    
      #第二列nq-3.23
      if n <= (r_max-q_row):   
         pg.click(x+c,y+(q_row-1+n)*f,duration=0.4)    #nq-data
      else:      
         pg.moveTo(s_x,s_y,duration=0.4)     
         pg.click(clicks=n-(r_max-q_row), interval=0.4)   #clicks=n-n_max
         pg.click(x+c,y+(r_max-1)*f,duration=0.4)    #y+(r_max-1)*f
         time.sleep(0.4)
       #第三行m  
      if m <= (r_max-m0_row):
         pg.click(x+2*c,y+(m0_row-1+m)*f,duration=0.4)   #nq-m副本  y+(m0_row-1+m)*f
      else:
         pg.moveTo(s_x,s_y,duration=0.4)     
         pg.click(clicks=m-(r_max-m0_row), interval=0.4)       #clicks=m-m_max
         pg.click(x+2*c,y+(r_max-1)*f,duration=0.4)   #y+(r_max-1)*f
      setfile = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\setfile.png', grayscale=False, confidence=0.6)
      time.sleep(0.5)
      #判断是否打开了配置文件
      if setfile != None:
         print("Find it")
         time.sleep(0.3)
      else:
         print(f'{n}q-{data}: {n}q  unclick   <配置文件>')
      #第五行配置文件
      #if m<=(r_max-m0_row-3):                  
         #pg.click(x+5*c,y+(m+5)*f,duration=0.4)      #配置文件
      #else:
         #pg.click(x+5*c,y+(r_max-1)*f,duration=0.4)
      pg.click(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\setfile.png', grayscale=False, confidence=0.6),duration=0.3)  #点击配置文件
      time.sleep(0.4)
      #确认
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.3)
      time.sleep(0.3)
      #发送
      #pg.click(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.4)
      time.sleep(0.3)
      print(f'{n}q-{data}: {n}{folder_name}({m})  发送成功')
      print('—————————————————————————————————')
      time.sleep(0.5)
      pg.click(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\#quicksend\code\minimize.png', grayscale=False, confidence=0.7),duration=0.4)
      m+=1
      time.sleep(0.5)
      
time.sleep(3600)
