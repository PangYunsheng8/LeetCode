# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解法一: 递归，时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def _build(preorder, inorder):
            if not preorder: return 

            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])

            root.left = _build(preorder[1: index + 1], inorder[: index])
            root.right = _build(preorder[index + 1: ], inorder[index + 1: ])
            return root

        return _build(preorder, inorder)
