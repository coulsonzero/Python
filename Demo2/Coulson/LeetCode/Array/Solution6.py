'''
lc 旋转数组
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
元素向右移动 k 个位置
'''


class Solution:
    @staticmethod
    def rotate(nums, k):
        """
        将其分开后合并
        print(nums[-k:]+nums[:-k]) 但无效 需要浅拷贝！
        """
        m = k % len(nums)
        nums[:] = nums[-m:] + nums[:-m]
        '''
        m = k % len(nums)
        # tmp = nums[:-m]
        # del nums[:-m]
        # return nums.extend(tmp)
        '''

        '''
        m = k % len(nums)
        nums[:] = nums[len(nums) - m:] + nums[:len(nums) - m]
        '''
