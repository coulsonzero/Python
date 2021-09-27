#计算两个数值公约数的数量
def func(m,n):
    i,count = 1,0
    while i <= min(m,n):
        if m % i == 0 and n % i == 0:
            count += 1
        i += 1
    print(count)

def input_mn():
    m, n = input("请输入两个数值，并用空格隔开：").split()
    if m.isdigit() and n.isdigit():
        func(int(m), int(n))
    else:
        print("请输入一串数字")


if __name__ == '__main__':
    input_mn()







