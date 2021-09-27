import pyautogui as pg


def click():
    while True:
        try:
            #pg.click(224,369)
            pg.press('s', interval = 3)
            pg.press('f', interval = 3)
            pg.press('c', interval = 3)
    
            print("finished")
        except ValueError:
            print("Ctrl + C")
click()


