# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(-1)
        pre, cur = node, head
        pre.next = head
        while cur:
            if cur.val == val: pre.next = cur.next
            else: pre = pre.next
            cur = cur.next
        return node.next
