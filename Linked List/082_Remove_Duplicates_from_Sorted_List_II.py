# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：直觉
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
        
#         """
#         if head == None:
#             return
#         elif head.next == None:
#             return head
        
#         _head = ListNode(0)
#         pre = _head
#         cur = head
#         while cur.next != None:
#             if cur.val == cur.next.val:
#                 while cur.val == cur.next.val and cur.next.next != None: cur = cur.next
#                 pre.next = cur.next
#             else:
#                 pre.next = cur
#                 pre = pre.next
            
#             if cur.next.next == None:
#                 break
#             cur = cur.next
            
#         if cur.val == cur.next.val:
#             pre.next = None
                
#         return _head.next
        

# 方法二：哈希表，感觉哈希表的方法写起来比较简单，但是耗时较长
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        def getHashMap(head):
            hashmap = {}
            cur = head
            while cur != None:
                hashmap[cur.val] = hashmap.get(cur.val, 0) + 1
                cur = cur.next
            return hashmap
        
        if head == None:
            return
        elif head.next == None:
            return head 
        
        hashmap = getHashMap(head)
        
        _head = ListNode(0)
        pre = _head
        cur = head
        while cur != None:
            while hashmap[cur.val] != 1 and cur.next != None: cur=cur.next
            if hashmap[cur.val] != 1:
                pre.next = None
            else:
                pre.next = cur
                pre = pre.next
            cur = cur.next

        return _head.next