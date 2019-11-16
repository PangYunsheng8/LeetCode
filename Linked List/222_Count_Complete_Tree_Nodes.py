# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一：层序遍历逐个统计。但是效率很低
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root: return 0
        num = 0
        stack = [root]
        while stack:
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            num += len(stack)
        return num + 1