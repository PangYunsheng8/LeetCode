# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        stack = [root]

        while stack:
            _res = [i.val for i in stack]
            res.append(_res)
        
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        return res
            
        
        
            
        