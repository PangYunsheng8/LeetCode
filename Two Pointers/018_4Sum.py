# 方法一：在3Sum的基础上加一个指针，直观方法，感觉大家也都是这么做的
# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         nums = sorted(nums)
#         res = []
#         for i in range(n-3):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, n-2):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 left = j + 1
#                 right = n - 1
#                 while left < right:
#                     value = nums[i] + nums[j] + nums[left] + nums[right]
#                     if value < target and left < right:
#                         left += 1
#                         while left < right and nums[left] == nums[left-1]: left+=1
#                     elif value > target and left < right:
#                         right -= 1
#                         while left < right and nums[right] == nums[right+1]: right-=1
#                     else:
#                         res.append([nums[i], nums[j], nums[left], nums[right]])
#                         left += 1
#                         while left < right and nums[left] == nums[left-1]: left+=1
#         return res

# 方法二：思路还是一样的，只是把数组换成了set，代码写起来更简洁一点，但是除了python可能其他语言就不能这么用了
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=set()
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):#固定两个数
                left=j+1#左指针
                right=len(nums)-1#右指针
                while(right>left):
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    if temp>target:right-=1#太大了，右指针左移
                    if temp<target:left+=1#反之
        return list(ans)
                        