import pyautogui as pg
import easyocr
import threading
from multiprocessing import Process
from PIL import ImageGrab
import time


alist = []

def screen_shot():
    x,y,m,n=770,325,850,380
    box=(x,y,m,n)
    im = ImageGrab.grab(box)
    im.save(r"C:\\Users\\21059\\Desktop\\ShopTians\\b.png")

def read():
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 开始识别图像")
    reader = easyocr.Reader(['ch_sim', 'en'])
    read_img = reader.readtext(r"C:\\Users\\21059\\Desktop\\ShopTians\\b.png")
    for i in read_img:
        world = i[1]
        world = world.replace('+', '')
        world = world.replace(',', '')
        world = world.replace("'", '')
        now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
        print(f"{now}: 商品打折能量为: {world}")
        alist.append(world)
        return alist


def Sell():
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 开始自动售卖")

    # 购买？
    buy = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\buy.png', grayscale=False, confidence=0.7)
    time.sleep(1)
    if buy != None:
        pg.press('s', interval=0.5)
        pg.press('c', interval=0.5)

    # 缺货？
    lack_supply = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\stockout.png', grayscale=False, confidence=0.7)
    time.sleep(1)
    if lack_supply != None:
        # time.sleep(7)
        pg.press('z', interval=1)
        print("refused: @缺货")
    else:
        # 闲聊
        pg.press('s', interval=1)
        success = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\success.png', grayscale=False, confidence=0.7)
        time.sleep(1)

        #闲聊失败
        if success == None:
            # time.sleep(8)
            pg.press('z', interval=0.5)
            print("refused: @闲聊失败")
        #闲聊成功
        else:
            # time.sleep(7)
            now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
            print(f"{now}: 开始判断价格")
            # 4.判断物价
            read()
            time.sleep(1)
            global price
            price = alist[0]
            print(f"商品的折扣能量：{price}")
            if int(price) < 330:
                print(">>> discount <<<")
                pg.press('e', interval=0.5)
                pg.press('c', interval=0.5)
                now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
                print(f"{now}: 已打折出售")
            elif int(price) > 860:
                pg.press('z', interval=0.5)
                pg.press('d', interval=0.5)

            else:
                pg.press('f', interval=0.5)
                time.sleep(2)
                suggest = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\suggest.png', grayscale=False, confidence=0.6)
                now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
                time.sleep(2)
                print(suggest)
                if suggest != None:
                    pg.press('c', interval=1)
                    print(f"{now}: >>> surcharge <<< ")
                else:
                    print(f"{now}:能量不够")
                    pg.click(pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\refuse.png', grayscale=False,confidence=0.6),interval=0.5)
                    pg.press('d', interval=1)
    # 重置数据
    alist.clear()
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 数据重置成功")
    print("========================================"+"\n")


def main():
    # read_thread = threading.Thread(target=read)
    # read_thread.start()
    screen_shot_thread = threading.Thread(target=screen_shot)
    screen_shot_thread.start()
    Sell_thread = threading.Thread(target=Sell)
    Sell_thread.start()


if __name__ == '__main__':
    while True:
        main1_p = Process(target=main)
        main1_p.start()
        main1_p.join(20)

    # main2_p = Process(target=main)
    # main2_p.start()
    # main2_p.join(19)


'''
识别10s
售卖17s
'''

