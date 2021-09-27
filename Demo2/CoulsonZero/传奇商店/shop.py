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






def Buy():
    img_buy = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\buy.png'
    img_confirm = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\confirm.png'
    while True:
        buy = pg.locateCenterOnScreen(img_buy, grayscale=False, confidence=0.7)
        time.sleep(0.5)
        if buy != None:
            print("ss")
            pg.press('c',interval=0.5)
            time.sleep(2)
            pg.click()
            confirm = pg.locateCenterOnScreen(img_confirm, grayscale=False, confidence=0.7)
            time.sleep(2)
            pg.click(confirm, interval=0.5)
        # else:
        #     print("unfind")
        #     continue




def Lack():
    # 缺货 - 市场 - 点击价格
    while True:

        #缺货？
        img_lack = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\lack.png'
        lack = pg.locateCenterOnScreen(img_lack, grayscale=False,confidence=0.7)
        time.sleep(1)


        if lack != None:
            print("正在补货 ")
            pg.click(lack, interval=0.5)
            time.sleep(1)

            p = 0
            #市场？
            img_market = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\market.png'
            market = pg.locateCenterOnScreen(img_market, grayscale=False,confidence=0.7)
            time.sleep(1)
            if market != None:
                print("市场")
                pg.click(market, interval=0.5)
                time.sleep(1)
                p=1

                #黄金价格
                img_clickbuy = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\clickbuy.png'
                clickbuy = pg.locateCenterOnScreen(img_clickbuy, grayscale=False,confidence=0.7)
                time.sleep(1)
                print(clickbuy)
                #购买

                if clickbuy != None:
                    print("正在用黄金购买")
                    pg.click(clickbuy, interval=0.5)
                    time.sleep(0.5)

                    l = 1
                    pop=True
                    while pop:
                        #需要再次购买？
                        clickbuy2 = pg.locateCenterOnScreen(img_clickbuy, grayscale=False,confidence=0.7)
                        if clickbuy2 != None:
                            print("继续购买")
                            pg.click(clickbuy2, interval=0.5)
                            time.sleep(1)
                            l += 1
                            if l < 9:
                                continue
                            elif l == 9:
                                img_cancle = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\cancle.png'
                                cancle = pg.locateCenterOnScreen(img_cancle, grayscale=False,confidence=0.7)
                                time.sleep(1)
                                pg.click(cancle, interval=0.5)
                                if p==1:
                                    pop=False
                                    continue
                                    # break
                        else:
                            print("只需购买一次")
                            time.sleep(2)

                    else:
                        print("市场未上架该商品")
                        # pg.click(lack, interval=0.5)
                        # img_make = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\make.png'
                        # make = cancle = pg.locateCenterOnScreen(img_make, grayscale=False,confidence=0.7)
                        # time.sleep(0.5)
                        # pg.click(make, interval=1)

                        # break
            # else:
            #     print("无法购买，准备制作")
            #     pass

        # else:
        #     print("库存充足")
        #     time.sleep(2)
        #     continue

def Lack2():
    Lack_t = threading.Thread(target=Lack)
    Lack_t.start()
    img_sell3 = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\sell3.png'
    sell3 = pg.locateCenterOnScreen(img_sell3, grayscale=False, confidence=0.7)
    pg.click(sell3,interval=1)
    time.sleep(3)
    img_continue1 = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\continue1.png'
    continue1 = pg.locateCenterOnScreen(img_continue1, grayscale=False, confidence=0.7)
    pg.click(continue1, interval=1)
    time.sleep(2)
    pg.press('d', interval=1)
    time.sleep(2)


def Sell():
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 开始自动售卖")

    img_lack = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\lack.png'
    lack = pg.locateCenterOnScreen(img_lack, grayscale=False, confidence=0.7)
    time.sleep(0.5)
    img_buy = r'C:\\Users\\21059\\Desktop\\ShopTians\\shop\\buy.png'
    buy = pg.locateCenterOnScreen(img_buy, grayscale=False, confidence=0.7)
    time.sleep(0.5)

    if lack==None and buy == None:
        pg.press('s', interval=1)
        success = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\success.png', grayscale=False,
                                          confidence=0.7)
        time.sleep(1)
        # 闲聊失败
        if success == None:
            pg.press('z', interval=0.5)
            print("refused: @闲聊失败")
        # 闲聊成功
        else:
            time.sleep(9)
            now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
            print(f"{now}: 开始判断价格")

            # 4.判断物价
            # global price
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
                suggest = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\suggest.png', grayscale=False,
                                                  confidence=0.6)
                now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
                time.sleep(1)
                if suggest != None:
                    pg.press('c', interval=1)
                    print(f"{now}: >>> surcharge <<< ")
                else:
                    print(f"{now}:能量不够")
                    pg.click(pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\refuse.png', grayscale=False,
                                                confidence=0.6), interval=0.5)
                    pg.press('d', interval=1)
    # 重置数据
    alist.clear()
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 数据重置成功")
    print("========================================" + "\n")


def main():
    read_thread = threading.Thread(target=read)
    read_thread.start()
    screen_shot_thread = threading.Thread(target=screen_shot)
    screen_shot_thread.start()
    Sell_thread = threading.Thread(target=Sell)
    Sell_thread.start()


if __name__ == '__main__':
    while True:
        Buy_t = threading.Thread(target=Buy)
        Buy_t.start()
        Lack2_t = threading.Thread(target=Lack2)
        Lack2_t.start()
        main_t = threading.Thread(target=main)
        main_t.start()
    # while True:
    #     main1_p = Process(target=main)
    #     main1_p.start()
    #     main1_p.join(20)


