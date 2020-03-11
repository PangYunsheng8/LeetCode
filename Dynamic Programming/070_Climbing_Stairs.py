# 状态f[n]: 到第n阶楼梯的所有方法
# 状态转移方程: f[n] = f[n-1] + f[n-2]
# 初始值和边界条件: f[0] = 0, f[1] = 1, f[2] = 2
# 计算顺序: 小->大

# 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def climbStairs(self, n):
        if n <= 2: return n 
        
        f = [0 for _ in range(n+1)]
        f[0], f[1], f[2] = 0, 1, 2

        for i in range(3, n+1):
            f[i] = f[i - 1] + f[i - 2]
        return f[-1]


if __name__ == "__main__":
    n = 6
    model = Solution()
    res = model.climbStairs(n)
    print(res)