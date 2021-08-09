import easyocr
import time

def now1():
    now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(now)
reader = easyocr.Reader(['ch_sim', 'en'])
read_img = reader.readtext(r"C:\Users\21059\Desktop\f.png")
for i in read_img:
    world = i[1]
    print(world)




