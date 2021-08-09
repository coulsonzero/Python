'''
lc 384. 打乱数组


给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

'''

import random, copy
# from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.copy = copy.copy(self.nums)

    def reset(self):
        self.copy = copy.copy(self.nums)
        return self.copy

    def shuffle(self):
        random.shuffle(self.copy)
        return self.copy

'''
class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()