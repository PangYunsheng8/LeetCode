# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def level_order(root):
            res = []
            stack = []
            if not root:
                return res
            stack.append(root)
            while stack:
                node = stack.pop(0)
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right and node.left:
                    stack.append(node.right)
                if node.right and node.left==None:
                    stack.append(node.right)
                    res.append("null")
            return res
        p_res = level_order(p)
        q_res = level_order(q)

        if p_res == q_res:
            return True
        else:
            return False
        