class Solution:
    def findPairs(self, nums, k: int) -> int:
        nums = sorted(nums)
        left, right = 0, 1
        res = 0
        while left < len(nums) and right < len(nums):
            if left == right:
                right += 1
                continue
            if abs(nums[right] - nums[left]) == k:
                res += 1
                right += 1
                while right < len(nums) and nums[right] == nums[right-1]: right += 1
            elif abs(nums[right] - nums[left]) < k:
                right += 1
                while right < len(nums) and nums[right] == nums[right-1]: right += 1
            elif abs(nums[right] - nums[left]) > k:
                left += 1
                while left < len(nums) and nums[left] == nums[left-1]: left += 1
        return res
            