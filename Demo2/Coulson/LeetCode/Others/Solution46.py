'''
lc 汉明距离

两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

输入：x = 3, y = 1
输出：1

'''


class Solution:
    '''
    思路：^异或位运算
    相同为0，不同为1，再统计1的个数
    '''
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
        # return bin(x^y)[2:].count('1')