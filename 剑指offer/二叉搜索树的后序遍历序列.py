# 递归分治，时间复杂度O(N^2)，空间复杂度O(N)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True

            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1

            return p == j and recur(i, m - 1) and recur(m, j - 1)
        return recur(0, len(postorder) - 1)