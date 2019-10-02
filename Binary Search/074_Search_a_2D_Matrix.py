class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix == []:
            return False
        # 先找到在哪一行
        col_low = 0
        col_high = len(matrix) - 1
        while col_low <= col_high:
            col_mid = (col_low + col_high) // 2
            if target >= matrix[col_mid][0] and target <= matrix[col_mid][-1]:
                break
            elif target < matrix[col_mid][0]:
                col_high = col_mid - 1
            else:
                col_low = col_mid + 1
        # 再找到在一行的哪个位置
        row_low = 0
        row_high = len(matrix[col_mid]) - 1
        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            if target == matrix[col_mid][row_mid]:
                return True
            elif target > matrix[col_mid][row_mid]:
                row_low = row_mid + 1
            else:
                row_high = row_mid - 1
        return False