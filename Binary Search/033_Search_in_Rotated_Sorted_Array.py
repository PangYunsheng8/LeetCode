class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            # 判断[low,mid]是升序还是旋转位
            if nums[low] <= nums[mid]:   # 升序
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:                       # 旋转位
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1   