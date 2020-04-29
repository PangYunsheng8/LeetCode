# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 基本思想:DFS迭代
class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        def recur(arr, root):
            if root.left and root.right:
                new_arr = arr.copy()
                arr.append(root.left.val)
                new_arr.append(root.right.val)
                recur(arr, root.left)
                recur(new_arr, root.right)
            elif root.left:
                arr.append(root.left.val)
                recur(arr, root.left)
            elif root.right:
                arr.append(root.right.val)
                recur(arr, root.right)
            else:
                if sum(arr) == sums: res.append(arr)

        res = []
        if not root: return res
        arrs = [root.val]
        recur(arrs, root)
        return res


# 基本思想:DFS递归
class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        
        res = []
        arr = []
        def dfs(root, arr):
            if not root: return
            if not root.left and not root.right and sum(arr) + root.val == sums: 
                res.append(arr + [root.val])
            
            dfs(root.left, arr + [root.val])
            dfs(root.right, arr + [root.val])
        dfs(root, arr)
        return res