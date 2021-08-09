'''
lc 两个数组的交集 II
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

思路：排序 双指针 移除特定元素
'''

class Solution:
    def intersect(self, nums1, nums2):
        '''
        遍历添加并删除,每次移除数组场长度都会发生动态变化，比较慢，虽然简洁
        '''
        return [nums1.pop(nums1.index(i)) for i in nums2 if i in nums1]

    '''
        # 双指针 40ms 85.35%
        nums1.sort()  # [4,5,9]
        nums2.sort()  # [4,4,8,9,9]
        a = []
        i = j = 0
        while i < len(nums2) and j < len(nums1):
            if nums2[i] == nums1[j]:
                a.append(nums2[i])
                i += 1
                j += 1
            elif nums1[j] > nums2[i]:
                i += 1
            else:
                j += 1
        return a
    '''