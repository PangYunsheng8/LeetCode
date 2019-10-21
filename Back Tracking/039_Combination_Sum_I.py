class Solution:
    def combinationSum(self, candidates, target: int):
        if not candidates: return []
        n = len(candidates)
        candidates = sorted(candidates)
        res = []
        path = []
        
        def dfs(begin, target):
            if target == 0:
                res.append(path[:])
            
            for index in range(begin, n):
                residue = target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                dfs(index, residue)
                path.pop()
        
        dfs(0, target)
        return res
        