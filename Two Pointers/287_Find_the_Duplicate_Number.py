# 方法一：哈希表，用哈希表解决本题是很简单的，但是关键在于改题目的要求是空间复杂度为O(1)，因此哈希表不满足改题目的要求
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         myhash = []
#         for i in range(len(nums)):
#             if nums[i] not in myhash: myhash.append(nums[i])
#             else: return nums[i]

# 方法二：快慢指针，之前遇到过一次快慢指针，这种题的解法思路还是很新颖的
class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break
                
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder: break
        
        return finder