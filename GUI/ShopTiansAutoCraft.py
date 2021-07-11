import pyautogui as pg
import time
import threading


def Ready():
    while True:
        img_ready = r'C:\\Users\\21059\\Desktop\\ShopTians\\craft1\\ready.png'
        ready = pg.locateCenterOnScreen(img_ready, grayscale=False,confidence=0.8)
        time.sleep(0.3)
        # 发现就绪
        if ready != None:
            pg.doubleClick(ready, interval=0.5)
            print("就绪")
            time.sleep(0.5)
        else:
            time.sleep(0.3)
            print("等待就绪")

def Collect():

    while True:
        img_collect = r'C:\\Users\\21059\\Desktop\\ShopTians\\craft1\\collect.png'
        collect = pg.locateCenterOnScreen(img_collect, grayscale=False,
                                          confidence=0.7)
        time.sleep(0.3)
        if collect != None:
            print("find 收集")
            pg.click(collect, interval=0.5)
            time.sleep(0.5)
        else:
            print("unfind 收集")

def Craft():
    while True:
        img_ready = r'C:\\Users\\21059\\Desktop\\ShopTians\\craft1\\ready.png'
        ready2 = pg.locateCenterOnScreen(img_ready, grayscale=False, confidence=0.8)
        time.sleep(1)
        print("ready",ready2)

        img_second = r'C:\\Users\\21059\\Desktop\\ShopTians\\craft1\\second.png'
        second = pg.locateCenterOnScreen(img_second, grayscale=False,confidence=0.8)
        time.sleep(1)
        print("second",second)

        if ready2 == None and second == None:
            # print("hello")
            print("全部制作完毕,开始制作新装备")
            pg.press ('space', interval=1)
            img_T1 = r'C:\\Users\\21059\\Desktop\\ShopTians\\craft1\\T1.png'
            T1 = pg.locateCenterOnScreen(img_T1, grayscale=False, confidence=0.6)
            pg.doubleClick(T1, duration=0.5)
            pg.click(clicks=9, interval=0.5)
            print("正在制作T1")
        else:
            print("正在制作中，请稍后")
            continue
if __name__ == '__main__':
    time.sleep(2)


    Ready_t = threading.Thread(target=Ready)
    Ready_t.start()

    Collect_t = threading.Thread(target=Collect)
    Collect_t.start()

    Craft_t = threading.Thread(target=Craft)
    Craft_t.start()
