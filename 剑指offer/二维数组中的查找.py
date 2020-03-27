# 时间复杂度: O(M+N), 空间复杂度: O(1)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        m, n = len(matrix), len(matrix[0])

        row, col = 0, n - 1
        while col >=0 or row <= m - 1:
            if target == matrix[row][col]: return True
            elif target > matrix[row][col]: 
                if row >= m - 1: return False
                row += 1
            elif target < matrix[row][col]: 
                if col <= 0: return False
                col -= 1          

        return False      

        