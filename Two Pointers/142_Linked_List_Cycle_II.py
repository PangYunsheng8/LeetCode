# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一:哈希表,这道题中感觉hash还是挺快的
# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         myset = set()
#         cur = head
#         while cur != None:
#             if cur in myset:
#                 return cur
#             myset.add(cur)
#             cur = cur.next
#         return None

# 方法二:快慢指针：两次相遇，第一次快慢指针相遇后，利用头节点到入环起始点的距离等于入环起始点到相遇点的距离这一特性
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return None
        slow = fast = find = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while find != fast:
                    find = find.next
                    fast = fast.next
                return find
        return None