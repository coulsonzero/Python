'''
lc 买卖股票的最佳时机 II
input: prices = [7,1,5,3,6,4]
output: 7

标签：数组 贪心 动态规划
'''
class Solution:
    '''
    思路：贪心算法（计算后一天与前一天的利润，正值则累加）
    '''
    def maxProfit(self, prices) -> int:
        sum = 0
        for i in range(len(prices)-1):
            sum += max(prices[i+1]-prices[i], 0)
        return sum