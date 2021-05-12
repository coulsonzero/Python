from PIL import ImageGrab
import time
import easyocr

time.sleep(3)
x,y,m,n=805,345,850,370
box=(x,y,m,n)
im = ImageGrab.grab(box)
im.save(r"C:\\Users\\21059\\Desktop\\ShopTians\\a.png")

reader = easyocr.Reader(['ch_sim', 'en'])
read_img = reader.readtext(r"C:\\Users\\21059\\Desktop\\ShopTians\\a.png")
for i in read_img:
    world = i[1]
    print(world)
    world = world.replace('+','')
    print(world)
    new = world.replace(',','')
    print(new)
    if int(new) > 1000:
        print("T11")
    elif int(new) < 100:
        print("<T3")
