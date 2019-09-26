class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[high] >= nums[mid]:
                high = mid
            else:
                low = mid + 1
        return nums[low]


class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        if nums[low] > nums[mid]:
            high = mid
        elif nums[low] == nums[mid]:
            if nums[low] > nums[high]:
                return nums[high]
            else:
                return nums[low]
        elif nums[low] < nums[mid] and nums[mid] < nums[high]:
            return nums[low]
        else:
            low = mid + 1
                
            mid = (low + high) // 2