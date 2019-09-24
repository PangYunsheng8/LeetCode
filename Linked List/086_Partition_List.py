# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：直觉
# class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         if head == None:
#             return 
#         elif head.next == None:
#             return head
        
#         cur, pre = head, ListNode(0)
#         _head = pre
#         right, right_head = None, None
#         while cur != None:
#             if cur.val >= x:
#                 if right == None:
#                     right = cur
#                     right_head = right
#                 else:
#                     right.next = cur
#                     right = right.next
#             else:
#                 pre.next = cur
#                 pre = pre.next  
#             cur = cur.next
        
#         if right_head != None:
#             _cur = right_head
#             while _cur.next != None:
#                 if _cur.next.val < x:
#                     _cur.next = None
#                     break
#                 _cur = _cur.next
            
#         pre.next = right_head
        
#         return _head.next

# 方法二：其实和方法一是一样的，只是在after链表中加入了哑结点，少了很多判断
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        cur = head
        while cur != None:
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next
            cur = cur.next
        after.next = None
        before.next = after_head.next
        
        return before_head.next