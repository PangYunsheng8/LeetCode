# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用队列来解决。以[0,2,4,1,null,3,-1,5,1,null,6,null,8]为例：
# 1)stack: [0] popleft         nodes: [0] popleft 
# 2)stack: [2,4] pop           nodes: [4,2] pop
# 3)stack: [1,3,-1] popleft    nodes: [1,3,-1] popleft
# 4)stack: [5,1,6,8] pop       nodes: [8,6,1,5] pop
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = collections.deque()
        stack.append(root)
        res = []
        flag = True
        while stack:
            _res = []
            nodes = collections.deque()
            for i in range(len(stack)):
                if flag: node = stack.popleft()
                else: node = stack.pop()
                _res.append(node.val)
                nodes.append(node)
            while nodes:
                if flag: node = nodes.popleft()
                else: node = nodes.pop()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            res.append(_res)
            flag = not flag
        return res
