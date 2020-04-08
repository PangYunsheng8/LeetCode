# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：栈。时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next

        node = ListNode(-1)
        pre = node
        while stack:
            value = stack.pop()
            pre.next = ListNode(value)
            pre = pre.next
        return node.next

# 方法二：递归。时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(head):
            if not head or not head.next: return head
            cur = recur(head.next)
            # 如果链表是1->2->3->4->5,那么此时cur=head.next就是5,head是4
            head.next.next = head
            head.next = None
            return cur
        return recur(head)

# 方法三：双指针。时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        return pre