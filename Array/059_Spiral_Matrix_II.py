class Solution:
    def generateMatrix(self, n):
        mat = [[0 for i in range(n)] for j in range(n)]

        l, r, t, b = 0, n - 1, 0, n - 1
        num, tar = 0, n * n
        while num < tar:
            for i in range(l, r + 1):
                num += 1
                mat[t][i] = num
            t += 1
            for i in range(t, b + 1):
                num += 1
                mat[i][r] = num
            r -= 1
            for i in range(r, l - 1, -1):
                num += 1
                mat[b][i] = num
            b -= 1
            for i in range(b, t - 1, -1):
                num += 1
                mat[i][l] = num
            l += 1
        return mat

    
model = Solution()
mat = model.generateMatrix(3)
print(mat)
