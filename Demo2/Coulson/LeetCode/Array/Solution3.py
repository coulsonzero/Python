'''
lc 存在重复元素
输入: [1,2,3,1]
输出: true

标签： 数组 排序 哈希表
'''


class Solution:
    '''
    1.排序后比较前后两项是否相等，相等则返回true
    2.比较集合去重后的数组是否相同
    3.比较集合去重后数组的长度
    '''
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
        # return len(nums) != len(set(nums))
        # return sorted(nums) != sorted(set(nums))