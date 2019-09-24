# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         cur_l1, arr_l1 = l1, []
#         cur_l2, arr_l2 = l2, []
#         while cur_l1 != None:
#             arr_l1.append(cur_l1.val)
#             cur_l1 = cur_l1.next
            
#         while cur_l2 != None:
#             arr_l2.append(cur_l2.val)
#             cur_l2 = cur_l2.next
        
#         num1 = ""
#         for i in range(1, len(arr_l1)+1):
#             num1 += str(arr_l1[-i])
            
#         num2 = ""
#         for j in range(1, len(arr_l2)+1):
#             num2 += str(arr_l2[-j])
        
#         new_num = int(num1) + int(num2)
        
#         new_num_reverse = ""
#         for k in range(1, len(list(str(new_num)))+1):
#             new_num_reverse += str(new_num)[-k]
        
#         link = ListNode(0)
#         link_head = link
#         i = 0
#         while i < len(new_num_reverse):
#             link.next = ListNode(new_num_reverse[i])
#             link = link.next
#             i += 1
        
#         return link_head.next


# 方法二：双指针
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        link = ListNode(0)
        link_head = link
        carry = 0
        while l1 != None or l2 != None:
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            
            link.next = ListNode(value)
            link = link.next
            
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        
        if carry:
            link.next = ListNode(carry)
            
        return link_head.next