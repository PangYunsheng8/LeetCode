class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
          
        for i in rows:
            for j in range(w):
                matrix[i][j] = 0
        for i in range(h):
            for j in cols:
                matrix[i][j] = 0