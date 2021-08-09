## ReverseInteger

**For Examples**
```
input: x = 123
output: 321

input: x = -123
output = -321

input = 120
output = 21

input: x = 0
output: 0
```

**题目要求**
> 如果反转后整数超过32位的有符号整数的范围[-2^31, 2^31 -1]，就返回0

**解题思路**
* 正整数直接转换为字符串切片反转即可；
* 负数保留"-"号，将后半部分转换为字符串切片反转；
* 如果反转后的整数超过范围就返回0
***
```python
class Solution:
    def reverse(selfself, x):
        num = int(str(abs(x))[::-1])
        s = -num if x<0 else num
        return s if -2**31 <= s <= 2**31-1 else 0
```


```
if x < 0:
    num = int(str(x)[1:][::-1])
```