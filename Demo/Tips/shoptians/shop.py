import pyautogui as pg

'''
思路：截图定位并点击
注意：图片不能放于文件夹内，只能放在桌面，否则运行错误
创建循环:
def click():
    while True:
click()
'''

def click():
    while True:
        try:
            pg.click(pg.locateCenterOnScreen('talk.png'))
            pg.click(pg.locateCenterOnScreen('surcharge.png'))
            pg.click(pg.locateCenterOnScreen('sell.png'))
        
        except:
            print("读取失败，请将图片从文件夹内移至桌面!")
click()

#之前还可以用，现在截图无法读取
#循环终止出错
