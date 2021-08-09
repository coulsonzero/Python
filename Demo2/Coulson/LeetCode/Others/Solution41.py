'''
lc 位1的个数

输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）
输入必须是长度为 32 的 二进制串 。

输入：00000000000000000000000000001011
输出：3


执行用时：28 ms, 在所有 Python3 提交中击败了99.06%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了70.36%的用户
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 第一种解法 使用python特性 bin(3) = ob11
        return bin(n).count("1")

        # return sum(1 for i in range(32) if n & (1 << i))
    '''
        # 第二种使用 位运算 特性 & 与预算符号，  >> 右进位预算符号
        res = 0
        while n:
            res += n & 1  
            n >>= 1 
        return res
    '''

    '''
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret
    '''

    '''
        ones = 0
        while n > 0:
            ones += 1
            n &= n - 1
        return ones
    '''