# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_l1 = l1
        cur_l2 = l2
        new_link = ListNode(0)
        cur = new_link
        
        while cur_l1 != None and cur_l2 != None:
            if cur_l1.val <= cur_l2.val:
                cur.next = cur_l1
                cur_l1 = cur_l1.next
            else:
                cur.next = cur_l2
                cur_l2 = cur_l2.next
            cur = cur.next
        if cur_l1 == None:
            cur.next = cur_l2
        elif cur_l2 == None:
            cur.next = cur_l1
        
        return new_link.next