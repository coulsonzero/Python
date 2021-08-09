'''
lc 实现 strStr()

输入：haystack = "hello", needle = "ll"
输出：2

在haystack字符串中找出needle字符串出现的第一个位置（下标从 0 开始)。如果不存在，则返回-1 。

标签： 双指针 字符串  字符串匹配
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)