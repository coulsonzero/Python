'''
lc 杨辉三角

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

思路：while s[i][j] != 1: s[i][j] = s[i-1][j-1]+s[i-1][j]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

    '''
        a = []
        for i in range(numRows):
            temp = [1] * (i+1)
            for j in range(0,i+1):
                if j == 0 or j == i:
                    continue
                temp[j] = a[i-1][j-1]+a[i-1][j]
            a.append(temp)
        return a
    '''