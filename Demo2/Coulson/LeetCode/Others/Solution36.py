# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


'''
lc 278. 第一个错误的版本

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
'''

class Solution:
    def firstBadVersion(self, n):
        # 二分法
        left = 1
        right = n
        while (left < right):
            mid = left + (right-left)//2
            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid+1
        return left