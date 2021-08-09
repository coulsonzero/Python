
'''
lc 有效的括号

输入：s = "()[]{}"
输出：true
输入：s = "([)]"
输出：false
输入：s = "{[]}"
输出：true


思路：栈(后进先出/先进后出)
执行用时：36 ms, 在所有 Python3 提交中击败了87.38%的用户
'''

class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={ ')':'(',']':'[','}':'{' }
        for i in s:
            if i in d and len(a)!=0 and a[-1]==d[i]:
                a.pop()
            else:
                a.append(i)
        return True if len(a)==0 else False
