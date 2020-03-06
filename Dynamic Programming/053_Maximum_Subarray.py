# 时间复杂度O(N),空间复杂度O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


# 时间复杂度O(N),空间复杂度O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)