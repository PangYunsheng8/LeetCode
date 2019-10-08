def threeSumClosest(nums, target):
    nums = sorted(nums)
    n = len(nums)
    error = float('inf')
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right: 
            sum = nums[i] + nums[left] + nums[right]
            if abs(sum-target) < error:
                error = abs(sum-target)
                final_sum = sum
            if sum > target:
                right = right - 1
            elif sum < target:
                left = left + 1
            else:
                return sum
    return final_sum

nums = [1,1,1,0]
target = -100
sum = threeSumClosest(nums, target)
print(sum)

        