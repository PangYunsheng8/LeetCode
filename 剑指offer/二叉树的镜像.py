# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：遍历每个结点，调换左右子树，时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(node):
            if not node: return
            node.left, node.right = node.right, node.left
            recur(node.left)
            recur(node.right)
        recur(root)
        return root


        