# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum1: int):
        res = []
        temp = []
        
        def dfs(root, sum1, temp):

            if not root: return 
            if not root.left and not root.right and sum1-root.val == 0: 
                temp += [root.val]
                res.append(temp)
            
            dfs(root.left, sum1-root.val, temp+[root.val])
            dfs(root.right, sum1-root.val, temp+[root.val])
            
        dfs(root, sum1, temp)
        
        return res