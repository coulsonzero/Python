'''
lc 198. 打家劫舍

输入：[2,7,9,3,1]
输出：12

input: [2,1,1,2]
output; 4
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]

    '''
        last = 0 
        now = 0
        for i in nums: 
            #这是一个动态规划问题
            last, now = now, max(last + i, now)
        return now
    '''
