# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return 
        elif head.next == None:
            return head
        
        cur = head
        sec_pointer = cur.next
        pre = None
        while cur.next != None:  
            sec = cur.next 
            cur.next = sec.next
            sec.next = cur
            if pre != None:
                pre.next = sec
            pre = cur
            cur = cur.next
            if cur == None:
                break
        
        head = sec_pointer
        return head