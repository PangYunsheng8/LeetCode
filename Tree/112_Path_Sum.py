# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum1: int) -> bool:
        if not root: return False
        if not root.left and not root.right and sum1-root.val == 0: return True
        return self.hasPathSum(root.left, sum1-root.val) | self.hasPathSum(root.right, sum1-root.val)

class Solution1:
    def hasPathSum(self, root: TreeNode, sum1: int) -> bool:
        path = []
        res = False
        
        def dfs(node):
            if not node: 
                if sum(path) == sum1:
                    res = True
                    print(res)
                return
            
            path.append(node.val)
            dfs(node.left)
            dfs(node.right)
            path.pop()
            
        dfs(root)
        
        return res

        
        