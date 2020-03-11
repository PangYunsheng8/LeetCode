class Solution:
    def minimumTotal(self, triangle):
        m, n = len(triangle), len(triangle[-1])
        f = [[0 for _ in range(n)] for _ in range(m)]
        f[-1] = triangle[-1]

        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
        return f[0][0]

if __name__ == "__main__":
    model = Solution()
    triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
    res = model.minimumTotal(triangle)
    print(res)
