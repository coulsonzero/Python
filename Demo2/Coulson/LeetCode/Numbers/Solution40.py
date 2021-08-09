'''
lc 罗马数字转整数

I             1
V             5
X             10
L             50
C             100
D             500
M             1000

输入: "IV"
输出: 4
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
输入: "MCMXCIV"
输出: 1994
解释: M = 1000; C=100, M=1000 CM = 900; X=10, C=100,XC = 90; IV = 4.

1000 -100 1000 -10 100 -1 5

思路：当后面一个罗马数字大于前一个数字则减
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans