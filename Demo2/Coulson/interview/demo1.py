from icecream import ic
'''
# 同行者第4题
n个人围成一圈从1开始报数，报到m的人出队，继续循环报数直至最后一人，求最后留下的人的编号
'''

n, m = map(int, input("n, m: ").split(","))
a = list(range(1, n+1))

for i in range(len(a)-1):
    del a[(m % len(a))-1]     # len(a)长度会动态变化, 从1开始所以减1
ic(a)
'''
for i in range(len(a)-1):
    del a[m%(n-i)-1]
print(a)


'''


