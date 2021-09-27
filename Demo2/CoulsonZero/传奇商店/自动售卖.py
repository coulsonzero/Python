import pyautogui as pg
import time
import easyocr
import threading

def now1():
    now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(now)

def read():
    print("开始识别图像：")
    now1()
    reader = easyocr.Reader(['ch_sim', 'en'])
    read_img = reader.readtext(r"C:\\Users\\21059\\Desktop\\ShopTians\\f.png")
    for i in read_img:
        world = i[1]
        print(f"商品打折能量为：",world)
        print("图像识别结束：")
        now1()
        return world


def Sell(world):
    time.sleep(1)
    print("开始自动售卖：")
    now1()
    time.sleep(9)
    # 点击
    # click(x,y)
    #1. 闲聊
    smalltalk = pg.press('s', interval = 1)
    print("正在闲聊：")
    now1()
    #失败（识别”适得其反“）--拒绝z
    result_smalltalk = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\fail.png', grayscale=False, confidence=0.7)
    time.sleep(1)
    print("正在识别闲聊是否成功")
    now1()
    if result_smalltalk != None:
        print("闲聊失败")
        pg.press('z', interval = 1)
    else:
        print("闲聊成功")
        # 2. 判断价格--打折/双倍
        if int(world) < 300:
            pg.press('e', interval=1)
        else:
            pg.press('f', interval=1)
        # 3.识别
        print("价格已识别")
        supply = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\stockout.png', grayscale=False, confidence=0.7)
        time.sleep(1)
        print("定位是否缺货")
        if supply != None:
            pg.press('z', interval=1)
            print("缺货！")
        else:
            pg.press('c', interval=1)
            print("成功出售")
        print("结束时间:")
        now1()

if __name__ == '__main__':

    sub2_thread = threading.Thread(target=Sell, args=[300])
    sub2_thread.start()
    sub1_thread = threading.Thread(target=read)
    sub1_thread.start()
'''
识别10s
售卖23s
'''

