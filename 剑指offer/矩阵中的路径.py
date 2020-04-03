# DFS+剪枝, 时间复杂度O(MN*3^K), 空间复杂度O(K)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # 下上右左
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            temp = board[i][j]
            board[i][j] = "/"
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False