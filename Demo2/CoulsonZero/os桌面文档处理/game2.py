#使用cmd-python获取鼠标实时位置
import pyautogui, sys
print('press ctrl-c to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'x: ' + str(x).rjust(4) +'Y: ' + str(y).rjust(4)
        print(positionStr,end = '')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')
