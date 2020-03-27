# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一: 递归，时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        node = head
        res = []

        def tra(node):
            if not node: return 
            tra(node.next)
            res.append(node.val)
        tra(node)

        return res

# 解法二: 迭代(栈)，时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        node = head
        stack, res = [], []

        # push
        while node:
            stack.append(node)
            node = node.next
        # pop
        while stack: 
            _node = stack.pop()
            res.append(_node.val)

        return res


