
'''
lc 合并两个有序数组

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n


输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m+n] = nums2[:n]
        nums1.sort()

'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.53%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了74.33%的用户
'''