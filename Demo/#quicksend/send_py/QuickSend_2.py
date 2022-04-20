import os, time, sys
import pyautogui as pg


time.sleep(1)
pg.confirm(text='''
使用小提醒：
0.管理员权限运行
1.请将软件安装包放于桌面文件夹"quciksend";执行文件夹置于桌面
2.请将<数字开头的其他无关文件夹>名称更改！！！
3.其他窗口最小化或者请移动至屏幕边缘以遮蔽最小化按钮！
4.拔掉U盘，
以免影响识别

ps: 鼠标移动至屏幕左上角几秒可停止运行程序''',title='使用注意',buttons=['已认真阅读','点击三次退出'])
data=pg.prompt(text='文件夹日期<3.19>：',title='输入框',default='')
folders_nums=int(pg.prompt(text='文件夹总数<1-8>',title='输入框',default=''))
t=int(pg.prompt(text='副本末尾数<1-8>：',title='输入框',default=''))


time.sleep(1)
x,y,f,m=800,413,20,2    #导航格窗口左上角起始坐标(x,y) f为每行、每列递增值    m为副本名称，t为副本末尾数
flodername = 'quicksend'

for n in range(1,folders_nums+1):
   #1q-3.19 1q
   os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q\QuickSend.exe'.format(flodername,n,data,n))
   time.sleep(1)
   abnormal = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\abnormal.png', grayscale=False, confidence=0.7)
   if abnormal != None:
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
      time.sleep(1)
   else:
      pass
   time.sleep(2)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(0.5)
   select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.7)
   time.sleep(1)
   if select != None:
      print("Find it")
   else:
      print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
   pg.click(x,y+2*f,duration=0.4)      #电脑 
   pg.click(x,y+(n+2)*f,duration=0.4)  #1q-3.19
   pg.click(x+f,y+2*f,duration=0.4)    #1q
   pg.click(x+4*f,y+5*f,duration=0.4)  #配置文件
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(0.5)
   #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(1)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
   print(f'{n}q-3.19: {n}q             发送成功')
   
   
   

   

   #1q-3.19 1q-副本
   os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q - 副本\QuickSend.exe'.format(flodername,n,data,n,m))
   time.sleep(1)
   abnormal = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\abnormal.png', grayscale=False, confidence=0.7)
   if abnormal != None:
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
      time.sleep(1)
   else:
      pass
   time.sleep(2)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(0.5)
   select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.7)
   time.sleep(1)
   if select != None:
      print("Find it")
   else:
      print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
      time.sleep(1)
   pg.click(x,y+2*f,duration=0.4)      
   pg.click(x,y+(n+2)*f,duration=0.4)  
   pg.click(x+f,y+3*f,duration=0.4)   
   pg.click(x+4*f,y+6*f,duration=0.4) 
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(0.5)
   #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.3)
   time.sleep(1)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.3),duration=0.3)
   print(f'{n}q-3.19: {n}q - 副本      发送成功')
   
   
   

   #1q-3.19 1q-副本(2)
   for m in range(2,t+1):
      os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q - 副本 ({})\QuickSend.exe'.format(flodername,n,data,n,m))
      time.sleep(1)
      abnormal = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\abnormal.png', grayscale=False, confidence=0.7)
      if abnormal != None:
         pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
         time.sleep(2)
      else:
         pass
      time.sleep(3)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.3)
      time.sleep(0.5)
      select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.5)
      time.sleep(1)
      if select != None:
         print("Find it")
      else:
         print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
      pg.click(x,y+2*f,duration=0.4)     
      pg.click(x,y+(n+2)*f,duration=0.4)  
      pg.click(x+f,y+(m+2)*f,duration=0.4)
      if m<5:
         pg.click(x+4*f,y+(m+5)*f,duration=0.4)  
      else:
         pg.click(x+4*f,y+10*f,duration=0.4)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.3)
      time.sleep(0.5)
      #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.3)
      time.sleep(1)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
      print(f'{n}q-3.19: {n}q - 副本 ({m})  发送成功')
      m+=1
      time.sleep(1)
      
time.sleep(1200)
#2questions:
#1.QuickSend.py.exe读取太慢
#2.身份弹窗
      
