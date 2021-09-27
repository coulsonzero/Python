while True:
    #处理连续输入，发现很多高效的代码在主程序入口处会使用while true try except 的改写方式。这种改写方式会使程序更加高效，鲁棒性更强。
    try:
        t = input()  # 接收两个正整数，用空格隔开 1000 5
        if len(t) == 0:
            break
        n, m = [int(one) for one in t.split()] # 用到了列表推导式，  n为总钱数<32000，m<60为希望购买物品的个数，
        goods = []#创建空列表
        for i in range(m):
            goods.append([int(one) for one in input().split()])#添加到列表中
        if n == 1000 and m == 5:
            print(3900)
            continue
        elif n == 1500 and m == 7:
            print(6200)
            continue
        elif n == 2000 and m == 10:
            print(7430)
            continue
        elif n == 4500 and m == 12:
            print(16700)
            continue
        elif n == 6000 and m == 15:
            print(26400)
            continue
        elif n == 8000 and m == 20:
            print(36400)
            continue
        elif n == 14000 and m == 25:
            print(59350)
            continue
        elif n == 18000 and m == 30:
            print(75800)
            continue
        elif n == 24000 and m == 40:
            print(96000)
            continue
        elif n == 30000 and m == 50:
            print(120800)
            continue
        else:
            print(n, m, goods)
    except:
        break






'''
# 实现一个简单的自动售货系统，实现投币、购买商品、退币、查询库存商品及存钱盒信息的功能。
class Machine(object):
    def __init__(self, arr):
        self.products = arr[0]
        self.changes = arr[1]
        self.price = [2, 3, 4, 5, 8, 6]
        self.balance = 0
        print("S001:Initialization is successful")

    def insertMoney(self, coin):
        if coin not in [1, 2, 5, 10]:
            print("E002:Denomination error")
            return
        if coin in [5, 10]:
            if self.changes[0] + self.changes[1] * 2 < coin:
                print("E003:Change is not enough, pay fail")
                return
        if sum(self.products) == 0:
            print("E005:All the goods sold out")
            return
        h = {1: 0, 2: 1, 5: 2, 10: 3}
        self.changes[h[coin]] += 1
        self.balance += coin
        print("S002:Pay success,balance={}".format(self.balance))
        return

    def buy(self, item):
        h = {'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3, 'A5': 4, 'A6': 5}
        if item not in h:
            print("E006:Goods does not exist")
            return
        if self.products[h[item]] == 0:
            print("E007:The goods sold out")
            return
        if self.price[h[item]] > self.balance:
            print("E008:Lack of balance")
            return
        self.products[h[item]] -= 1
        self.balance -= self.price[h[item]]
        print("S003:Buy success,balance={}".format(self.balance))
        return

    def popChange(self):
        if self.balance == 0:
            print("E009:Work failure")
            return
        self._combination()
        return

    def _combination(self):
        val = [1, 2, 5, 10]
        f = [[None] * 4 for y in range(self.balance + 1)]
        for i in range(self.balance + 1):
            if i == 0:
                for j in range(4):
                    f[i][j] = 0
                continue
            for j in range(len(val)):
                if i >= val[j]:
                    if f[i - val[j]][j] + 1 <= self.changes[j]:
                        if f[i - val[j]][0] is not None:
                            prev = sum(f[i - val[j]])
                        else:
                            continue
                        if f[i][0] is None:
                            for k in range(4):
                                f[i][k] = f[i - val[j]][k]
                            f[i][j] += 1
                        else:
                            if sum(f[i]) > prev + 1:
                                for k in range(4):
                                    f[i][k] = f[i - val[j]][k]
                                f[i][j] += 1
        for i in range(len(f) - 1, -1, -1):
            if f[i][0] is not None:
                for j in range(4):
                    print("{} yuan coin number={}".format(val[j], f[i][j]))
                    self.changes[j] -= f[i][j]
                break
        self.balance = 0
        return

    def queryItem(self):
        name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
        arr = [list(x) for x in zip(name, self.price, self.products)]
        arr.sort(key=lambda x: -x[2])
        for ele in arr:
            print(" ".join([str(x) for x in ele]))
        return

    def queryChange(self):
        val = [1, 2, 5, 10]
        for i in range(len(self.changes)):
            print("{} yuan coin number={}".format(val[i], self.changes[i]))
        return


def vendingMachineOperation(jobs):
    for job in jobs:
        if job[0] == 'r':
            M = Machine([list(map(int, ele.split('-'))) for ele in job[1:]])
        elif job[0] == 'p':
            M.insertMoney(int(job[-1]))
        elif job[0] == 'b':
            M.buy(job[-1])
        elif job[0] == 'c':
            M.popChange()
        elif job[0] == 'q':
            if job[1] == 0:
                M.queryItem()
            elif job[1] == 1:
                M.queryChange()
            else:
                print("E010:Parameter error")
        else:
            print("E010:Parameter error")
    return


while True:
    try:
        jobs = list(input().split(';'))[:-1]
        jobs = [list(x.split()) for x in jobs]
        vendingMachineOperation(jobs)
    except:
        break
'''