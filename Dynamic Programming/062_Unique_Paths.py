# 时间复杂度O(MN), 空间复杂度O(MN)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m - n == 0 and m == 1: 
            return 1

        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]

# 时间复杂度O(MN), 空间复杂度O(MN)，将边界条件初始化到数组中
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]

# 时间复杂度O(MN), 空间复杂度O(2N), 根据动态转移方程f[i][j] = f[i-1][j] + f[i][j-1]可知，只需要保留当前行和上一行即可
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j-1] + pre[j]
            pre = cur
        return cur[-1]

# 时间复杂度O(MN),空间复杂度O(N),道理同上
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]