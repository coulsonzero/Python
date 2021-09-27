import pyautogui as pg
pg.press('space', interval=1)
a=pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\T1.png', grayscale=False, confidence=0.7)
pg.moveTo(a,duration= 0.5)
pg.click(clicks=15,interval=1)
