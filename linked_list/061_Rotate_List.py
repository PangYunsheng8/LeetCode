# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def get_length(head):
            count = 0
            cur = head
            while cur != None:
                count += 1
                cur = cur.next
            return count
            
        if head == None: return 
        if head.next == None: return head
            
        count = get_length(head)
        step = k % count
        
        if step == 0: return head
    
        cur_pos = 0
        cur = head
        while cur_pos < (count - step - 1):
            cur = cur.next
            cur_pos += 1
        
        sec = cur.next
        _head = cur.next
        cur.next = None
        
        while sec.next != None: sec = sec.next
        sec.next = head
        
        return _head