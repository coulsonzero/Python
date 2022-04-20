'''
lc 删除排序数组中的重复项
input: nums = [0,0,1,1,1,2,2,3,3,4]
output: 5, nums = [0,1,2,3,4]

标签：数组 双指针 从后遍历删除
'''
class Solution:
    @staticmethod
    def removeDuplicates(nums):
        """
        删除则从后遍历数组
        比较前后两项是否相同，相同则删除即可
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)

    '''
    双指针
    当快指针与后一项不同时则交换快慢指针的值
    def removeDuplicates(self, nums):
        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return 0 if not nums else slow
    '''
if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution.removeDuplicates(nums))