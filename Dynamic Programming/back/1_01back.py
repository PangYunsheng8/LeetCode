# 状态: f[i][j]表示只看前i个物品，总体积是j的情况下，总价值是多少

# f[i][j]:
# 1.不选第i个物品，f[i][j] = f[i - 1][j]
# 2.选第i个物品，f[i][j] = f[i - 1][j - v[i]] + w[i]
# 状态转移方程: f[i][j] = max(f[i - 1][j], f[i][j] = f[i - 1][j - v[i]] + w[i])

# 初始化: f[0][0] = 0

# 二维DP,时间复杂度O(NV), 空间复杂度O(NV)
class ZeroOneBack2D:
    def zoback(self, N: int, Volume: int, V: list, W: list) -> int:
        m, n = N, Volume
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # 注意这里把N和Volume都加了1，是为了考虑没有item和体积为0的情况。
        for i in range(1, m+1): # 注意从1开始而不是0, 0是初始状态
            for j in range(1, n+1):
                dp[i][j] = dp[i - 1][j]
                if j - V[i-1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - V[i-1]] + W[i-1])
        return dp[-1][-1]

# 一维DP,时间复杂度O(NV),空间复杂度O()
class ZeroOneBack1D:
    def zoback(self, N: int, Volume: int, V: list, W:list) -> int:
        m, n = N, Volume
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            for j in range(n, -1, -1):
                if j >= V[i]:
                    dp[j] = max(dp[j], dp[j-V[i]] + W[i])
                print(dp[j])
        print(dp)
        return dp[-1]

if __name__ == '__main__':
    N, Volume = 4, 5
    V = [1, 2, 3, 4]
    W = [2, 4, 4, 5]

    # model = ZeroOneBack2D()
    model = ZeroOneBack1D()
    ans = model.zoback(N, Volume, V, W)
    print(ans)