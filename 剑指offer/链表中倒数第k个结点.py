# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一，时间复杂度O(N), 空间复杂度O(1)
# 思路：先遍历链表，计算出链表长度，再获得倒数第k个结点的正数index，重新遍历链表直到index
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        num = 0
        node = head
        while node:
            num += 1
            node = node.next
        
        index = 1
        node_k = head
        while index <= (num - k):
            node_k = node_k.next
            index += 1
        return node_k

# 解法二，时间复杂度O(N), 空间复杂度O(1)
# 思路：双指针。两个指针pre, cur相距k个结点，每次同时移动，若cur为None时，pre刚好为第k个结点
# 时间复杂度解析，对于cur，需要先提前走k个结点，再和pre走(length - k)个结点，length为链表长度，
# 因此时间复杂度为O(N), 相比较于第一种，时间复杂度没有减少，但是实际的运行时间会减少。
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        node = head
        while k > 0:
            node = node.next
            k -= 1
        pre, cur = head, node
        while cur:
            cur = cur.next
            pre = pre.next
        return pre