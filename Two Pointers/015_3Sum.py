class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                target = nums[left] + nums[right] + nums[i]
                if target < 0:
                    left += 1
                    while nums[left] == nums[left-1] and left < right: left+=1
                elif target > 0:
                    right -= 1
                    while nums[right] == nums[right+1] and left < right: right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right: left+=1
        return res