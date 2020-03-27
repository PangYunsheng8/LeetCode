# 解法一: 哈希表, 时间复杂度O(n), 空间复杂度O(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        myhash = {}
        for i in range(len(nums)):
            myhash[nums[i]] = myhash.get(nums[i], 0) + 1
            if myhash[nums[i]] > 1: return nums[i]


# 解法二: 排序, 时间复杂度O(nlogn), 空间复杂度O(1)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: return nums[i]


# 解法三: 原地置换，时间复杂度O(n), 空间复杂度O(1)
# 思路: 如果一个排好序的数组，且无重复，那么下标i就等于num[i]。从头遍历数组，若遇到下标i不等于num[i],就将
# num[num[i]]与num[i]调换，若两者相等，则说明重复，返回该元素。
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] == nums[nums[i]]: return nums[i]
                else: 
                    temp = nums[i]
                    nums[i] = nums[nums[i]]
                    nums[temp] = temp
