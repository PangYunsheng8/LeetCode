class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for i in range(len(nums) - 1):
            if i == 0:
                res.append(str(nums[i]))
                continue

            if nums[i + 1] - nums[i] == 1:
                continue
            elif nums[i] - nums[i - 1] == 1:
                




            
