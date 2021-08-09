## ReverseStringList

**input:**
```
s = ['c', 'o', 'u', 'l', 's', 'o', 'n']
```
**output**
```
['c', 'o', 'u', 'l', 's', 'o', 'n']
```
**题目要求：**
```
原地修改：空间复杂度O(1)
```
**思路**
* 原地反转
    * str.reverse() 
    * 双指针法
* 使用额外空间
    * s[::-1]
    * reversed(s)
***
```python
class Soultion:
    def reverseString(self, s):
        # str.reverse()
        return s.reverse()

        # 双指针法
        l, r = 0, len(s-1)
        while l < r:
            s[l], s[r] = s[l], s[r]
            l += 1
            r -= 1
        return s

        '''
        额外空间反转
        # 切片
        return s[::-1]  # 最快
        return list(reversed(s))
        '''
```