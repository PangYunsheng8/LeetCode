# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一：直觉, 时间复杂度O(MN), 空间复杂度O(1)
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        # 判断t1是否包含t2
        def isSub(t1, t2):
            # 下面其实是几种可能的情况
            # 1)第一种t1为None, t2不为None, 说明t1不包含t2，返回False
            if t2 and not t1: return False
            # 2)第二种t2为None,那t1无所谓，结果都是True
            if not t2: return True
            # 3)第三种是t1和t2都不为None,需要分两种情况，t1.val是否等于t2.val
            # 若等于，继续向下判断
            if t1.val == t2.val: 
                return isSub(t1.left, t2.left) and isSub(t1.right, t2.right)
            # 若不等于，返回False
            else: 
                return False

        # 遍历t1每个结点，并逐个判断是否包含t
        def iteration(t1, t):
            # 包含，直接返回True
            if isSub(t1, t): return True
            else: 
                # 若直到t1为None，那肯定不包含，返回False
                if not t1: return False
                # 否则需要继续向下迭代每个结点，注意这里是or，只要有一个包含就返回True
                return iteration(t1.left, t) or iteration(t1.right, t) # 注意：python的or有阻断效应，只要or左右出现一个True,程序不再向下执行，直接返回True
        return iteration(A, B)
