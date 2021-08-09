'''
lc 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
'''

class Solution:
    '''
    解题思路：
    1.前后查找索引
    2.计数统计

    '''
    def firstUniqChar(self, s: str) -> int:
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1
    '''
    执行用时：100 ms, 在所有 Python3 提交中击败了82.12%的用户
    '''
    '''
        tmp = collections.Counter(s)
        for i in range(len(s)):
            if tmp[s[i]] == 1:
                return i
        return -1
    '''
