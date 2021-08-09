'''
lc 缺失数字

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list(range(len(nums)+1)))-sum(nums)
'''
执行用时：40 ms, 在所有 Python3 提交中击败了94.09%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了67.93%的用户
'''