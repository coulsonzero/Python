import pyautogui as pg
import easyocr
import threading
from multiprocessing import Process
from PIL import ImageGrab
import time


alist = []
def screen_shot():
    x,y,m,n=780,325,850,370
    box=(x,y,m,n)
    im = ImageGrab.grab(box)
    im.save(r"C:\\Users\\21059\\Desktop\\ShopTians\\b.png")

def read():
    screen_shot()
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 开始识别图像")
    reader = easyocr.Reader(['ch_sim', 'en'])
    read_img = reader.readtext(r"C:\\Users\\21059\\Desktop\\ShopTians\\b.png")
    for i in read_img:
        world = i[1]
        print(world)
        world = world.replace('+', '')
        world = world.replace('-', '')
        world = world.replace(',', '')
        world = world.replace("'", '')
        world = world.replace("I", '')
        now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
        print(f"{now}: 商品打折能量为: {world}")
        alist.append(world)
        return alist

def Sell():
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
    print(f"{now}: 开始自动售卖")

    # 购买？
    buy = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\buy.png', grayscale=False, confidence=0.7)
    time.sleep(0.5)
    if buy != None:
        pg.press('s', interval=0.5)
        pg.press('c', interval=0.5)

    # 缺货？
    lack_supply = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\stockout.png', grayscale=False, confidence=0.7)
    time.sleep(0.5)
    if lack_supply != None:
        pg.press('z', interval=0.3)
        print("refused: @缺货")
    else:
        # ocr
        read()
        time.sleep(1)
        global price
        try:
            price = alist[0]
            if price != None:
                now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
                print(f"{now}: 开始判断")
                # 打折能量<300
                if int(price) < 330:
                    # <300, 则打折
                    print(">>> discount")
                    pg.press('s', interval=0.5)
                    time.sleep(2)
                    success = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\success.png', grayscale=False,
                                                      confidence=0.6)
                    time.sleep(2)
                    # 闲聊成功--折扣-出售
                    if success != None:
                        print("闲聊成功")
                        pg.press('e', interval=0.5)
                        pg.press('c', interval=0.5)
                        print(">>> discount出售 <<<")
                    # 闲聊失败--拒绝
                    else:
                        pg.press('z', interval=0.5)
                        print("refused: @闲聊失败")
                #打折能量>=300
                else:
                    # 点击额外收费
                    pg.press('f', interval=0.5)
                    time.sleep(2)
                    # 建议？
                    suggest = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\suggest.png', grayscale=False,
                                                      confidence=0.8)
                    time.sleep(1)
                    #没有建议--额外收费-出售
                    if suggest == None:
                        print(suggest)
                        pg.press('s', interval=1)
                        pg.press('c', interval=1)
                        print(f"{now}: >>> surcharge <<< ")
                    # 有建议--闲聊-成功还是失败？
                    else:
                        print(suggest)
                        print(f"{now}:能量不足，继续闲聊")
                        pg.press('s', interval=0.5)
                    # 闲聊
                        success = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\success.png', grayscale=False,
                                                          confidence=0.6)
                        fail = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\fail.png', grayscale=False,confidence=0.6)
                        time.sleep(2)
                        # 闲聊成功-额外收费-出售

                        if fail == None:
                            print("闲聊成功")
                            pg.press('f', interval=0.5)
                            pg.press('c', interval=0.5)
                            print(">>> surcharge <<<")
                            time.sleep(1)
                        # 闲聊失败-拒绝
                        elif fail != None:
                            pg.press('z', interval=0.5)
                            print("refused: @闲聊失败")

                # 重置数据
                # global alist
                for i in alist:
                    if i==price:
                        alist.remove(price)
                now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
                print(f"{now}: 数据已重置")
                print("========================================"+"\n")
        except IndexError:
            now = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '%Y-%m-%d
            print(f"{now}出现异常，稍等1s")
            time.sleep(10)
            pg.click(500,314)
        # except:
        #     print("出现异常，稍等30s")
        #     time.sleep(30)
        #     pg.click(650,270)

def main():
    Sell_thread = threading.Thread(target=Sell)
    Sell_thread.start()
    Sell_thread.join()


if __name__ == '__main__':
    while True:
      main()





