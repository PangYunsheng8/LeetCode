# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：先遍历一遍链表，获得链表长度，然后把删除从后向前第n个元素，转变为删除从前向后的第length-n个元素
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         def length(head):
#             count = 0
#             cur = head
#             while cur != None:
#                 count += 1
#                 cur = cur.next
#             return count 
        
#         length_list = length(head)
#         reverse_n = length_list - n
        
#         if length_list == 1:
#             return 
        
#         if reverse_n == 0:
#             return head.next
#         else:
#             cur = head
#             cur_pos = 0
#             pre = None
#             while cur_pos < reverse_n:
#                 pre = cur
#                 cur = cur.next
#                 cur_pos += 1
#             pre.next = cur.next

#             return head

# 使用双指针，第一个指针开始指向n+1处，第二个指针指向head,同时移动两个指针，使得它们保持间隔为n，当第一个指针指向末尾时，
# 第二个指针指向的就是第n个元素
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return 
        
        cur_pos = 0 
        cur_first = head
        while cur_pos < n - 1:
            cur_first = cur_first.next
            cur_pos += 1
        
        cur_second = head
        pre = None
        while cur_first.next != None:
            pre = cur_second
            cur_first = cur_first.next
            cur_second = cur_second.next
        
        if pre == None:
            head = head.next
        else:
            pre.next = cur_second.next
        
        return head