'''
lc 有效的数独

输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
数独部分空格内已填入了数字，空白格用 '.' 表示
'''

# 列表判断法
class Solution:
    def isValidSudoku(self, board) -> bool:
        # 创建三个空数组
        row = [[] * 9 for _ in range(9)]
        col = [[] * 9 for _ in range(9)]
        nine = [[] * 9 for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp = board[i][j]
                # 如果不是数字/".", 跳过
                if not tmp.isdigit():
                    continue
                # 判断数字是否有效
                if tmp in row[i]:
                    return False
                if tmp in col[j]:
                    return False
                if tmp in nine[(j // 3) * 3 + (i // 3)]:
                    return False
                # 如果不在就添加进数组中
                row[i].append(tmp)
                col[j].append(tmp)
                nine[(j // 3) * 3 + (i // 3)].append(tmp)
        return True
'''
执行用时：44 ms, 在所有 Python3 提交中击败了94.26%的用户
'''


'''
字典计数法
class Solution:
    def isValidSudoku(self, board):
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True
'''