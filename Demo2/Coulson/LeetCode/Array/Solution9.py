
'''
lc 加一
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
输入：digits = [0]
输出：[1]
输入：[1,2,9]
输出：[1,3,0]
输入：[9,9]
输出：[1,0,0]
并不是所有都逢9进1，而是末尾逢九进1，直到不逢9就返回
'''
class Solution:
    def plusOne(self, digits):
        '''
        倒序遍历
        如果该项为9九变为0，前一项加一
        '''
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # 以下是数组全为9的情况
        digits.insert(0,1)
        return digits
