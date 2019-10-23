class Solution:
    def combine(self, n: int, k: int):
        if n < k: return []
        if n == 1: return [[1]]
        if k == 1: return [[i+1] for i in range(n)]
        
        res = []
        path = []
        
        def back_tracking(begin):
            if len(path) >= k:
                res.append(path[:])
                return
                
            for j in range(begin, n+1):
                path.append(j)
                back_tracking(j+1)
                path.pop()
        
        for i in range(1, n):
            path = [i]
            back_tracking(i+1)
        return res