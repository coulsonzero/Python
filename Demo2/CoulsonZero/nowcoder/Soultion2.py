while True:
    try:
        m = int(input('Examples: '))
        for k in range(m):
            n = int(input('Friends: '))
            s = input().split()
            aList = list(map(int, s))
            # 计算花费时间最短的出发坐标点
            # 求每个坐标点到其他坐标点的步数
            for i in aList:
                e = abs(sum(aList) - i*len(aList))


            b = [abs(sum(aList) - i*len(aList)) for i in aList]
            # 求出步数最少的坐标
            c = [index for index, j in enumerate(b) if j == min(b)]
            # 将符合要求的坐标输出(步数相同取最小值)
            d = [aList[p] for p in range(len(aList)) if p in c]
            print(min(d))
    except:
        break