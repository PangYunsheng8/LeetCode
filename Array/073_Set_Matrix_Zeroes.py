# 方法一:空间复杂度为O(m+n)的方法，通过记录0位置的行号和列号
# class Solution:
#     def setZeroes(self, matrix) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         rows = set()
#         cols = set()
#         h, w = len(matrix), len(matrix[0])
#         for i in range(h):
#             for j in range(w):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
          
#         for i in rows:
#             for j in range(w):
#                 matrix[i][j] = 0
#         for i in range(h):
#             for j in cols:
#                 matrix[i][j] = 0

# 方法二:空间复杂度为O(1)的方法，将应该置为0的元素先置为一个非法字符，再转换为0
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    for m in range(h):
                        if matrix[m][j] != 0:
                            matrix[m][j] = True
                    for n in range(w):
                        if matrix[i][n] != 0:
                            matrix[i][n] = True
        for i in range(h):
            for j in range(w):
                if type(matrix[i][j]) is bool:
                    matrix[i][j] = 0
        