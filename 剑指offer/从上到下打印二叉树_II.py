# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            _res = []
            nodes = []
            for i in range(len(stack)):
                node = stack.pop()
                _res.append(node.val)
                nodes.append(node)
            for i in range(len(nodes)-1, -1, -1):
                node = nodes.pop()
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
            res.append(_res)
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def recur(root, k):
            if root:
                if len(res) <= k:
                    res.append([])
                res[k].append(root.val)
                recur(root.left, k+1)
                recur(root.right, k+1)
        recur(root, 0)
        return res