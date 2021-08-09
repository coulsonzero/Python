'''
lc 字符串转换整数
输入：s = "words and 987"
输出：0
输入：s = "4193 with words"
输出：4193

整数范围 [−2^31, 2^31−1]
'''

import re
class Solution:
    def myAtoi(self, s):
        '''
        '^[+-]?\d+': 匹配可能以+或-开头的数字串
        '''
        return max(min(int(*re.findall('^[+-]?\d+', s.lstrip())), 2**31 - 1), -2**31)