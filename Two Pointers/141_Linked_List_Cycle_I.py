# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一:哈希表，注意这里用了set而没有用list，因为set的查找效率比list要高很多
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         myset = set()
#         cur = head
#         while cur != None:
#             if cur in myset:
#                 return True
#             else:
#                 myset.add(cur)
#             cur = cur.next
#         return False

# 方法二：快慢指针
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head or head.next == None:
#             return False
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if fast == None or fast.next == None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True

# 还是快慢指针，换了个写法而已，上面是参考别人的，下面是自己写的
class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while fast:
            if not fast.next or not fast.next.next: return False
            fast = fast.next.next
            slow = slow.next 
            if slow == fast: return True