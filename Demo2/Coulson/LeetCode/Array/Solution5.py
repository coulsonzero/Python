"""
lc 两数之和
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""


class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for i, v in enumerate(nums):
            if d.get(target - v) is not None:
                return [d[target - v], i]
            d[v] = i
        return [0, 0]


