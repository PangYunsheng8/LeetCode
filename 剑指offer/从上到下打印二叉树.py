# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            nodes = []
            for i in range(len(stack)):
                node = stack.pop()
                res.append(node.val)
                nodes.append(node)
            for i in range(len(nodes)-1, -1, -1):
                node = nodes.pop()
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
        return res

# 利用队列的先进先出来做
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = collections.deque()  
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res
