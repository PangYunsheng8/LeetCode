# class Solution:
#     def rotate(self, matrix) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
        
#         # 先按行调换位置
#         for i in range(n):
#             for j in range(n//2):
#                 matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
#         # 再置换
#         for i in range(n-1):
#             for j in range(n-i-1):
#                 matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]


# 方法二：直接旋转，这种做法太绕了，不推荐
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n//2):
            for j in range(i, n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp