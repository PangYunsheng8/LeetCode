# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        
        def _build(preorder, inorder):
            if len(preorder) == 0: return 
            
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            
            root.left = _build(preorder[1:index+1], inorder[:index])
            root.right = _build(preorder[index+1:], inorder[index+1:])
            return root
        return _build(preorder, inorder)
        
