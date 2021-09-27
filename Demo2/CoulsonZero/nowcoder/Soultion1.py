while True:
    try:
        # 输入一个整数C，表示测试实例的个数
        c = int(input('examples: '))
        for k in range(c):
            # 输入一个整数N，表示星星的个数
            n = int(input('stars: '))
            # 输入N个星星坐标：[(x1,y1), (x2,y2), ..., (xn,yn)]
            a = [tuple(map(int, input('x y: ').split())) for i in range(n)]
            # 判断正方形的个数
            lsum = rsum = 0
            if n >= 4:
                for i in range(len(a)):
                    lsum += a[i][0]
                    rsum += a[i][1]
                if lsum-rsum == 0:
                    print(n//4)
                else:
                    print(0)
            else:
                print(0)
    except:
        break

