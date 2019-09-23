# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        
        pre = head
        cur = head.next
        
        while cur != None:
            if cur.val == pre.val:
                cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        pre.next = None
        
        return head