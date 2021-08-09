'''
lc 只出现一次的数字
输入: [4,1,2,1,2]
输出: 4

思路： 集合 异或
标签： 位运算 数组
'''

class Solution:
    '''
    统计次数，再筛选出最少次数即第一个
    '''
    def singleNumber(self, nums):
        '''
        return reduce(lambda x, y: x ^ y, nums)
        '''

        '''
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sorted(d.items(), key=lambda x: x[1])[0][0]
        '''


    ''' 
    ^（异或）--相同为0，不同为1
    任何数和 00 做异或运算，结果仍然是原来的数，a^0 = a
    任何数和其自身做异或运算，结果是 0, a^a = 0
    异或运算满足交换律和结合律
        reduce = 0
        for num in nums: 
            reduce ^= num
        return reduce
    '''

    '''
    s = set()
    for i in nums:
        if i not in s:
            s.add(i)
        else:
            s.remove(i)
    for j in s:
        print(j)
    '''