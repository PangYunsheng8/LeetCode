# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        
        def _build(postorder, inorder):
            if len(postorder) == 0: return 
            
            n = len(postorder) - 1
            
            root = TreeNode(postorder[n])
            index = inorder.index(postorder[n])
            
            root.left = _build(postorder[:index], inorder[:index])
            root.right = _build(postorder[index:n], inorder[index+1:])
            
            return root
        
        
        return _build(postorder, inorder)