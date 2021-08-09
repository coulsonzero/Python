### 字符串反转
* str.reverse() 原地反转
* s[:] = s[::-1] 切片反转
* 双指针 交换

整数反转
```
num = int(str(abs(x))[::-1])
s = -num if x < 0 else num
```
查找字符
```
str.find()
str.rfind()
```
计数
```
tmp = collections.Counter(s)
for i in range(len(s)):
    if tmp[s[i]] == 1:
        return i
return -1
```
正则表达式
```
*re.findall('^[+-]?\d+', s.lstrip())
```

排序
sorted(str)
数组转字符串
''.join(b)

常用方法
split()
join()
replace()
eval()
isalnum()/isalpha()/isdigit()/isspace()/
isupper()/islower()

lower()/upper()/capitalize()/title()/swapcase()