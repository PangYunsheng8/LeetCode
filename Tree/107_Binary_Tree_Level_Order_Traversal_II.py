# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root: return []
        res = []
        stack = [root]
        
        while stack:
            _res = [i.val for i in stack]
            res.insert(0, _res)
            
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
        return res
        
        
        