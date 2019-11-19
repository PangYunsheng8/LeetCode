# 方法一：模拟
class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        temp = [[False for i in range(m)] for j in range(n)]

        for indice in indices:
            row = indice[0]
            col = indice[1]
            for j in range(m):
                temp[row][j] = bool(1-temp[row][j])
            for i in range(n):
                temp[i][col] = bool(1-temp[i][col])

        num = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == True: num+= 1
        return num

# 方法二：模拟+空间优化
class Solution1:
    def oddCells(self, n: int, m: int, indices) -> int:

        rows = [False] * n 
        cols = [False] * m
        for i, j in indices:
            rows[i] = bool(1 - rows[i])
            cols[j] = bool(1 - cols[j])
        
        print(rows)
        print(cols)
        num = 0
        for i in range(n):
            for j in range(m):
                if (rows[i] ^ cols[j]) == True: num += 1
        return num