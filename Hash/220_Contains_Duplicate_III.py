class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if k == 0 or t < 0: return False
        all_buckets = {}
        bucket_size = t + 1
        for i in range(len(nums)):
            # 放在哪个桶
            cur_bucket = nums[i] // bucket_size
            
            # 判断当前桶是否有元素
            if cur_bucket in all_buckets: return True
            # 判断前面的桶是否有满足的元素
            if (cur_bucket-1) in all_buckets and abs(all_buckets[cur_bucket-1] - nums[i]) <= t: return True
            # 判断后面的桶是否有满足的元素
            if (cur_bucket+1) in all_buckets and abs(all_buckets[cur_bucket+1] - nums[i]) <= t: return True
            
            all_buckets[cur_bucket] = nums[i]
            
            if i >= k:
                all_buckets.pop(nums[i-k]//bucket_size)