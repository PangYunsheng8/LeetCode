class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        
        if nums[mid] == target:
            mid_r = mid
            mid_l = mid
            while mid_r < len(nums) - 1:
                mid_r = mid_r + 1
                if nums[mid_r] != target:
                    mid_r = mid_r - 1
                    break
            while mid_l > 0:    
                mid_l = mid_l - 1
                if nums[mid_l] != target:
                    mid_l = mid_l +1
                    break

            return [mid_l, mid_r]
        else:
            return [-1, -1]
            