# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        
        def ToBST(nums, start, end):
            if start > end : return
            
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = ToBST(nums, start, mid-1)
            root.right = ToBST(nums, mid+1, end)
            return root
            
        start = 0
        end = len(nums) -1 
        
        return ToBST(nums, start, end)