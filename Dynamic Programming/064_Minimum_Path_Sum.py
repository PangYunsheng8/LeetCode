# 状态: f[i][j]: 到第(i,j)时的最短路径
# 状态转移方程: f[i][j] = min(f[i-1][j], f[i][j-1]) + g[i][j]
# 初始值和边界: f[0][0]

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == j == 0: f[i][j] = grid[i][j]
                elif i == 0: f[i][j] = f[i][j-1] + grid[i][j]
                elif j == 0:  f[i][j] = f[i-1][j] + grid[i][j]
                else:  f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        return f[-1][-1]

if __name__ == '__main__':
    grid = [[1,3,1], [1,5,1], [4,2,1]]
    mps = Solution()
    res = mps.minPathSum(grid)
    print(res)