class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        res = []
        r, b = len(matrix[0]), len(matrix)
        l, t = 0, 0
        while len(res) < len(matrix[0]) * len(matrix):
            for i in range(l, r): res.append(matrix[t][i])
            for j in range(t+1, b): res.append(matrix[j][r-1])
            if (b-1 > t) and (r-1 > l):
                for i in range(r-2, l, -1): res.append(matrix[b-1][i])
                for j in range(b-1, t, -1): res.append(matrix[j][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res    
        