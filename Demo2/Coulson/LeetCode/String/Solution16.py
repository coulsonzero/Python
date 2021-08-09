'''
lc 有效的字母异位词

输入: s = "anagram", t = "nagaram"
输出: true
输入: s = "rat", t = "car"
输出: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)