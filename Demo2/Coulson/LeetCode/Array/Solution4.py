"""
lc 移动零
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

标签：数组 双指针
"""


class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1


"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.60%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了89.39%的用户
"""