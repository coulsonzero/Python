'''
lc 48. 旋转图像

输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

要求：原地修改  顺时针旋转90度
'''


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 执行用时：32ms, 在所有Python3提交中击败了94.53 %的用户
        matrix[:] = list(map(list, zip(*matrix[::-1])))
        # matrix[:] = [list(x) for x in zip(*matrix[::-1])]


        '''
        # 解包 原地旋转
        for i, v in enumerate(zip(*matrix)):
            matrix[i] = list(v)
            matrix[i].reverse()
        '''

        '''
        # 解包 浅拷贝
        a = list(map(list, zip(*matrix)))
        for i in a:
            i.reverse()
        matrix[:] = a
        '''

        '''
        # 浅拷贝
        执行用时：32 ms, 在所有 Python3 提交中击败了94.53%的用户
        a = []
        b = []
        for j in range(len(matrix[0])):
            for i in range(len(matrix)-1, -1, -1):
                a.append(matrix[i][j])
            b.append(a[:])
            a.clear()
        matrix[:] = b
        return matrix[:]
        '''

        '''
        # 浅拷贝 双指针
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        '''

        '''
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        '''