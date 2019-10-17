# 方法一：使用hash表，只需一次遍历
class Solution:
    def isValidSudoku(self, board) -> bool:
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        seq = [[] for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] not in row[i]:
                    row[i].append(board[i][j])
                else:
                    return False
                
                if board[i][j] not in col[j]:
                    col[j].append(board[i][j])
                else:
                    return False
                
                if board[i][j] not in seq[(i//3)*3+j//3]:
                    seq[(i//3)*3+j//3].append(board[i][j])
                else:
                    return False
        return True
                