# 字符串反转
s = input()
print(s[::-1])


# 表达式求解
s = input()
print(eval(s))
print(eval(s.strip()))  # 删除空白字符


# 杨辉三角
repeat = [2, 3, 2, 4]
while True:
    try:
        n = int(input())
        print(-1) if n < 3 else print(repeat[n%4-3])
    except:
        break


# 日期计算
s = input()
year, month, day = map(int, s.split())
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4 == 0 and year%100 !=0) or (year%400==0):     # 判断闰年
    month_day[1] = 29
r = sum(month_day[:month-1]) + day
print(r)


# 计算公共字串长度
'''
输入：asdfas
      werasdfaswer
输出：6
'''
a = str(input())
b = str(input())
n = 0
for i in range(len(a)):
    if a[i-n:i+1] in b:
        n += 1
print(n)


# 统计大写字母的个数: str.isupper()
s = input()
cnt = 0
for i in s:
    if i.isupper():
        cnt += 1
print(cnt)


# 最长回文子串
'''
输入：cdabbacc
输出：4
说明：abba为最长的回文子串
'''
def fun(s):
    for i in range(len(s),-1,-1):
        for j in range(0,len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i
while True:
    try:
        s = input()
        if s:
            print(fun(s))
    except:
        break


# 计算n*m的棋盘格子有多少种走法
def f(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        return f(n-1, m)+f(n, m-1)

while True:
    try:
        n, m = map(int, input().split())
        print(f(n, m))
    except:
        break



# 参数解析
'''
输入：xcopy /s c:\\ d:\\
输出：4
      xcopy
      /s
      c:\\
      d:\\
'''
s = input()
flag = 0
start = end = i = sum = 0
res = []
while i < len(s):
    if s[i] == ' ':
        sum += 1
        end = i
        res.append(s[start:end])
        start = end + 1

    if s[i] == '"':
        start = i + 1
        flag = 1
        while flag == 1:
            i += 1
            if s[i] == '"':
                end = i
                flag = 0
                res.append(s[start:end])
                end = i = i + 1
                start = end + 1
    i += 1
if end < len(s):
    res.append(s[start:])
print(len(res))
for i in res:
    print(i)


# 尼科彻斯定理
'''
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
'''
m=int(input())
s=list(range(m*m-m+1, m*m+m, 2))
# print('+'.join(map(str, s)))
print(s)
print('+'.join(map(str, s)))

