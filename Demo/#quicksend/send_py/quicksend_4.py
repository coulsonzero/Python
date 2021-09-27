import os, time, sys
import pyautogui as pg

#弹窗提醒与输入
pg.confirm(text='''
一.使用小提醒：
0.管理员权限运行
1.请将待执行文件夹<1q-3.19>和软件安装包<code>放于桌面文件夹"quciksend"(可修改);
2.请将<数字开头的其他无关文件夹>名称更改！！！
3.其他窗口最小化或者请移动至屏幕边缘以遮蔽最小化按钮！
4.拔掉U盘，
以免影响识别!!!

二.影响识别成功率因素
A.网络延迟
B.身份弹窗
C.具体数据(需定制)

ps: 鼠标移动至屏幕左上角几秒可停止运行程序

——————————————————CoulsonZero——————————————————
''',title='使用注意',buttons=['我已仔细阅读','点击三次退出'])

data=pg.prompt(text='待执行文件夹日期<3.19>',title='输入框',default='')
folders_nums=int(pg.prompt(text='待执行文件夹总数',title='输入框',default=''))
t=int(pg.prompt(text='副本末尾数<max:8> ',title='输入框',default=''))

#设定初始值
time.sleep(1)  #导航格窗口左上角起始坐标(x,y)  
x,y,f,m=800,413,20,2     #m为副本名称，t为副本末尾数, f为每行、每列递增值,不通尺寸屏幕f始终不变
flodername = 'quicksend'
User=21059  #Administrator



# n个待执行文件夹
for n in range(1,folders_nums+1):
    #打开QuickSend.exe
    os.startfile(r'C:\Users\{}\Desktop\{}\{}q-{}\{}q\QuickSend.exe'.format(User,flodername,n,data,n))
    time.sleep(1)
    #识别有无身份登录异常弹窗
    abnormal = pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\abnormal.png'.format(User,flodername), grayscale=False, confidence=0.7)
    if abnormal != None:
        #如果有异常--> 点击确认
        pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\confirm.png'.format(User,flodername), grayscale=False, confidence=0.6),duration=0.5)
        time.sleep(2)
    else:
        pass
    time.sleep(3)
    #点击<选择配置>
    pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\select.png'.format(User,flodername), grayscale=False, confidence=0.7),duration=0.3)
    #按‘Enter’再次点击<选择配置>
    pg.press('enter')
    time.sleep(0.5)
    #监视是否进去<选择配置> 并反馈信息
    select = pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\spot.png'.format(User,flodername), grayscale=False, confidence=0.5)
    time.sleep(1)
    if select != None:
        print("Find it")
    else:
        print(f'{n}q-3.19: {n}q<选择配置>点击失败,请稍后重试')
    #关闭<此电脑>目录
    pg.click(x,y+2*f,duration=0.4)     #根据不同电脑导航栏位置需要修改数据
    #打开<执行文件1q-3.16目录>
    pg.click(x,y+(n+2)*f,duration=0.4)  #根据不同执行文件起始导航栏位置需要修改数据
    for m in range(0,t+1):
        #打开1q-3.16副本目录
        pg.click(x+f,y+(m+2)*f,duration=0.4)  #根据不同执行文件副本起始导航栏位置  可能需要修改数据
        if m<5:
            #如果副本（m）< 5
            pg.click(x+4*f,y+(m+5)*f,duration=0.4)   #根据不同执行文件副本起始导航栏位置  可能需要修改数据
        else:
            #如果副本 (m) > 5
            pg.click(x+4*f,y+10*f,duration=0.4)  #根据不同执行文件副本起始导航栏位置  可能需要修改数据
        m+=1
        #点击<确认>
        pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\confirm.png'.format(User,flodername), grayscale=False, confidence=0.7),duration=0.3)
        time.sleep(0.5)
        #点击<发送>
        pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\{}\code\send.png'.format(User,flodername), grayscale=False, confidence=0.7),duration=0.3)
        time.sleep(1)
        #点击<窗口最小化>
        pg.doubleClick(pg.locateCenterOnScreen(r'C:\Users\{}\Desktop\flodername\code\minimize.png'.format(User,flodername), grayscale=False, confidence=0.6),duration=0.5)
        print(f'{n}q-3.19: {n}q - 副本 ({m})  发送成功')
        
        time.sleep(1)
#反馈---复查有无遗漏
time.sleep(1200)  
    
#位置修改：电脑/文件夹/副本目录
#(x,y)  电脑
#(x,y+4*f)  1q-3.19
#(x+f,y+3*f)  1q副本
#              配置文件
