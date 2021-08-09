'''
lc 验证回文串

输入: "A man, a plan, a canal: Panama"
输出: true
输入: "race a car"
输出: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        b = ''
        for i in s.lower():
            if i.isalnum():
                b += i
        '''

        b = [i for i in s.lower() if i.isalnum()]
        b = ''.join(b)

        i = 0
        j = len(b)-1
        while i < j:
            if b[i] != b[j]:
                return False
            i += 1
            j -= 1
        return True
    '''
    执行用时44 ms, 在所有 Python3 提交中击败了96.42%的用户
    '''
