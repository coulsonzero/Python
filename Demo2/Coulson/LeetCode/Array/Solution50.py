'''
lc 53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6

解释：
贪心：若当前指针所指元素之前的和小于0，则舍弃当前元素之前的序列
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
        当前值：-1
        之前和：4
        当前和：3
        最大和：4
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
        """
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns
