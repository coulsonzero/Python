##**数组常用算法**
* 双指针
* (末尾)遍历(删除)
* 排序
* 贪心算法
* 集合去重
* 字典计数
* 切片
* 异或运算判断唯一不重复数
* 矩阵解包


双指针
```python
def removeDuplicates(self, nums):
    fast = slow = 1
    while fast < len(nums):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return 0 if not nums else slow
```
```python
def moveZeroes(self, nums):
    i = 0
    for j in range(0, len(nums)):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
```
```python
# 双指针 40ms 85.35%
nums1.sort()  # [4,5,9]
nums2.sort()  # [4,4,8,9,9]
a = []
i = j = 0
while i < len(nums2) and j < len(nums1):
    if nums2[i] == nums1[j]:
        a.append(nums2[i])
        i += 1
        j += 1
    elif nums1[j] > nums2[i]:
        i += 1
    else:
        j += 1
return a
```

末尾遍历(删除)
```python3
def removeDuplicates(self, nums):
    '''
    删除则从后遍历数组
    比较前后两项是否相同，相同则删除即可
    '''
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == nums[i-1]:
            del nums[i]
    return len(nums)
```

```python
for i in range(len(digits)-1, -1, -1):
    if digits[i] != 9:
        digits[i] += 1
        return digits
    else:
        digits[i] = 0
# 以下是数组全为9的情况
digits.insert(0,1)
return digits
```


排序
nums.sort()
```python
def containsDuplicate(self, nums) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```
贪心算法
```python
def maxProfit(self, prices) -> int:
    sum = 0
    for i in range(len(prices)-1):
        sum += max(prices[i+1]-prices[i], 0)
    return sum
```

集合去重
```python
return len(nums) != len(set(nums))
```

```python
return sorted(nums) != sorted(set(nums))
```

字典计数
```python
def twoSum(self, nums, target):
    d = dict()
    for i, v in enumerate(nums):
        if d.get(target - v) != None:
            return [d[target - v], i]
        d[v] = i
    return [0, 0]
```
```python
d = dict()
for i in nums:
    d[i] = d.get(i, 0) + 1
return sorted(d.items(), key=lambda x: x[1])[0][0]
```


切片
```python
m = k % len(nums)
nums[:] = nums[-m:] + nums[:-m]
```

```python
matrix[:] = list(map(list, zip(*matrix[::-1])))
# matrix[:] = [list(x) for x in zip(*matrix[::-1])]
```

位运算  
* ^（异或）--相同为0，不同为1
* 任何数和 00 做异或运算，结果仍然是原来的数，a^0 = a
* 任何数和其自身做异或运算，结果是 0, a^a = 0
```python
return reduce(lambda x, y: x ^ y, nums)
```

解包
```python
a = list(map(list, zip(*matrix)))
for i in a:
    i.reverse()
matrix[:] = a
```