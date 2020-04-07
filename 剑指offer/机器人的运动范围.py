# 思路，典型的DFS+剪枝, 空间复杂度O(mn), 时间复杂度O(mn)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def cal(num):
            res = 0
            for i in list(str(num)):
                res += int(i)
            return res

        res = set()
        def _dfs(i, j):
            if i >= m or j >= n or (cal(i) + cal(j)) > k or (i, j) in res: return
            res.add((i, j))

            _dfs(i + 1, j)
            _dfs(i, j + 1)

        _dfs(0, 0)
        return len(res)