# 双指针, 时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while nums[l] % 2 == 1 and l < r: l += 1
            while nums[r] % 2 == 0 and l < r: r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        return nums