'''
lc 3的幂
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return int((math.log10(n)/math.log10(3)) % 1 == 0
        # return (n > 0 and 1162261467 % n == 0)
        '''
        if n > 1:
            while n % 3 == 0:
                n /= 3
        return n == 1
        # 执行用时：6 ms, 在所有 Python3 提交中击败了95.96%的用户
        '''
