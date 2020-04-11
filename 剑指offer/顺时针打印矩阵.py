class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        t, b, l, r = 0, m - 1, 0, n - 1
        res = []

        while len(res) < m*n:
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            for j in range(t, b+1): res.append(matrix[j][r])
            r -= 1
            if b > t - 1 and r > l - 1:
                for i in range(r, l-1, -1): res.append(matrix[b][i])
                b -= 1
                for j in range(b, t-1, -1): res.append(matrix[j][l])
                l += 1
        return res

