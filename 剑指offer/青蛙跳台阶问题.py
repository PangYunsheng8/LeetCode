# 经典DP, 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1: return 1
        f = [0 for _ in range(n + 1)]
        f[0] = 1
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[-1] % 1000000007