'''
lc 爬楼梯

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''


class Solution:
    '''
    def climbStairs(self, n: int) -> int:

        if n <= 1:
            return 1
        if n < 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # 超时
        '''
    def climbStairs(self, n: int) -> int:
        return self.Fibonacci(n, 1, 1)
    def Fibonacci(self, n, a ,b):
        if n <= 1:
            return b
        return self.Fibonacci(n - 1, b, a + b)