import os, time, sys
import pyautogui as pg
time.sleep(1)
pg.confirm(text='''
1.请将文件夹和软件安装包放于桌面文件夹"quciksend"，图片放于子文件夹Code内!!!;
2.请将数字开头的其他无关文件夹名称更改！！！
3.其他窗口最小化或者请移动至屏幕边缘以遮蔽最小化按钮！以免影响识别;
ps: 鼠标移动至屏幕左上角停止运行''',title='提醒框',buttons=['OK','Cancle'])
           
flodername = 'quicksend'
data=pg.prompt(text='文件夹日期<3.19>：',title='输入框',default='')
folders_nums=int(pg.prompt(text='文件夹总数：',title='输入框',default=''))
t=int(pg.prompt(text='副本末尾数：',title='输入框',default=''))


time.sleep(1)
x,y,f,m=800,413,20,2    #导航格窗口左上角起始坐标(x,y) f为每行、每列递增值    m为副本名称，t为副本末尾数


for n in range(1,folders_nums+1):
   #1q-3.19 1q
   os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q\QuickSend.exe'.format(flodername,n,data,n))
   time.sleep(3)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.6)
   if select != None:
      print("Find it")
      time.sleep(1)
   else:
      print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
   pg.click(x,y+2*f,duration=0.5)      #电脑 
   pg.click(x,y+(n+2)*f,duration=0.5)  #1q-3.19
   pg.click(x+f,y+2*f,duration=0.5)    #1q
   pg.click(x+4*f,y+5*f,duration=0.5)  #配置文件
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
   print(f'{n}q-3.19: {n}q            发送成功')
   time.sleep(1)

   

   #1q-3.19 1q-副本
   os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q - 副本\QuickSend.exe'.format(flodername,n,data,n,m))
   time.sleep(3)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.6)
   if select != None:
      print("Find it")
      time.sleep(1)
   else:
      print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
   pg.click(x,y+2*f,duration=0.5)      
   pg.click(x,y+(n+2)*f,duration=0.5)  
   pg.click(x+f,y+3*f,duration=0.5)   
   pg.click(x+4*f,y+6*f,duration=0.5) 
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.5)
   time.sleep(1)
   pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
   print(f'{n}q-3.19: {n}q - 副本      发送成功')
   time.sleep(1)
   

   #1q-3.19 1q-副本(2)
   for m in range(2,t+1):
      os.startfile(r'C:\Users\Administrator\Desktop\{}\{}q-{}\{}q - 副本 ({})\QuickSend.exe'.format(flodername,n,data,n,m))
      time.sleep(3)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\select.png', grayscale=False, confidence=0.7),duration=0.5)
      time.sleep(1)
      select = pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\spot.png', grayscale=False, confidence=0.6)
      if select != None:
         print("Find it")
         time.sleep(1)
      else:
         print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
      pg.click(x,y+2*f,duration=0.5)     
      pg.click(x,y+(n+2)*f,duration=0.5)  
      pg.click(x+f,y+(m+2)*f,duration=0.5)    
      if m<5:
         pg.click(x+4*f,y+(m+5)*f,duration=0.5)  
      else:
         pg.click(x+4*f,y+10*f,duration=0.5)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\confirm.png', grayscale=False, confidence=0.7),duration=0.5)
      time.sleep(1)
      #pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\send.png', grayscale=False, confidence=0.7),duration=0.5)
      time.sleep(1)
      pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\Administrator\Desktop\quicksend\code\minimize.png', grayscale=False, confidence=0.6),duration=0.5)
      print(f'{n}q-3.19: {n}q - 副本 ({m})  发送成功')
      time.sleep(1)
      m+=1
