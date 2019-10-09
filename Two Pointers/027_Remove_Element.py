# 方法：双指针（快慢指针）
class Solution:
    def removeElement(self, nums, val: int) -> int: 
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        n = len(nums)
        i = 0
        for j in range(n):
            print(nums)
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i