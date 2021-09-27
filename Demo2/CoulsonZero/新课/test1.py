

import keyboard
from PIL import ImageGrad
import time
import aip_content_recongnition
path=r'C:\Users\21059\Desktop\Tips\screen.png'
keyboard.wait(hotkey = 'ctrl+alt+a')
time.sleep(3)
image = ImageGrad.grabclipboard()
if image:
    image.save(path)
    result = aip_content_recongnition.get_info_from_image(path)



# 应用：自动阅卷系统