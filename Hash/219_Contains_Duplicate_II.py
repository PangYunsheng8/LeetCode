class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                if (i - temp[nums[i]]) <= k: return True
            temp[nums[i]] = i  #本题最精妙之处在于此，由于我们需要的是last index，因此这里保证了当前的index就是last index。
        return False