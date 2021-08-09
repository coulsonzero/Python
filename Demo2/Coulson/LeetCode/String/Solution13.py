'''
lc 整数反转

输入：x = 123
输出：321
输入：x = -123
输出：-321
输入：x = 120
输出：21
输入：x = 0
输出：0
'''


class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        s = -num if x < 0 else num
        return s if -2**31 <= s <= 2**31-1 else 0