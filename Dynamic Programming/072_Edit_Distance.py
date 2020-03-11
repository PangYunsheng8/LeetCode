# 状态: f[i][j]: word1的第i个字符到word2的第j个字符的编辑距离
# 状态转移方程: f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1, f[i-1][j-1] + flag), flag = 1 or 0
# 初始值和临界条件: f[0][0] = 0
# 计算顺序: 小->大

# 时间复杂度O(MN),空间复杂度O(MN)
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        f = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0: f[i][j] = max(i, j)
                else:
                    flag = 1 if word1[i-1] != word2[j-1] else 0
                    f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + flag) 
        return f[-1][-1]


if __name__ == '__main__':
    ed = Solution()
    res = ed.minDistance('intention', 'execution')
    print(res)