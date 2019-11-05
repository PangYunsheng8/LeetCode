# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一: 直觉想出来的，先中序遍历，再创建链表，但是不是原地算法
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         res = []
#         def inorder(root):
#             if not root: return 
#             res.append(root.val)
#             inorder(root.left)
#             inorder(root.right)
#         inorder(root)
        
#         for i in range(1, len(res)):
#             root.left = None
#             _node = TreeNode(res[i])
#             root.right = _node
#             root = root.right

# 方法二：递归，原地算法，空间复杂度为O(1)
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root: return 
            dfs(root.left)
            dfs(root.right)
            
            if root.left:
                if root.right:
                    node = root.left
                    while node.right: node = node.right
                    node.right = root.right
                root.right = root.left
                root.left = None
        
        dfs(root)
            
            
            