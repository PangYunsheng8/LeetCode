# 状态: f[i][j]: 到第(i,j)时的最短路径
# 状态转移方程: f[i][j] = min(f[i-1][j], f[i][j-1]) + g[i][j]
# 初始值和边界: f[0][0]

# 时间复杂度O(MN), 空间复杂度O(1), 直接在原数组上存储，不占用额外的数组空间
class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i-1][j] + grid[i][j]
                else:  grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


# 时间复杂度O(MN), 空间复杂度O(1), 直接在原数组上存储，不占用额外的数组空间
class Solution2:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


# 时间复杂度O(MN), 空间复杂度O(N), 不修改入参
class Solution3:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        cur = [0 for _ in range(n)]
        cur[0] = grid[0][0]
        for i in range(1, n):
            cur[i] = cur[i-1] + grid[0][i]

        for i in range(1, m):
            for j in range(n):
                if j == 0: cur[j] = cur[j] + grid[i][j]
                else: cur[j] = min(cur[j], cur[j-1]) + grid[i][j]
        return cur[-1]


if __name__ == '__main__':
    grid = [[1,3,1], [1,5,1], [4,2,1]]
    # mps = Solution()
    # mps = Solution2()
    mps = Solution3()
    res = mps.minPathSum(grid)
    print(res)