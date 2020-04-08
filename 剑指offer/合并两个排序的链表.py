# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l, r = l1, l2
        node = ListNode(-1)
        cur = node
        while l and r:
            if l.val > r.val: 
                cur.next, r = r, r.next
            else:
                cur.next, l = l, l.next
            cur = cur.next
        cur.next = l if l else r
        return node.next