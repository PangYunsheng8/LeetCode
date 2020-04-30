"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# 思路，中序遍历。时间复杂度O(N), 空间复杂度O(N), 最差情况下，即树退化为链表时，递归深度达到N，系统使用O(N)栈空间。
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def traversal(cur):
            if not cur: return

            traversal(cur.left)
            if not self.pre: 
                self.head = cur
            else:
                self.pre.right = cur
                cur.left = self.pre
            self.pre = cur
            traversal(cur.right)

        if not root: return None
        self.head, self.pre = None, None
        traversal(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
