class Solution:
    def permuteUnique(self, nums):
        res = []
        
        def back_tracking(num, temp):
            if not temp:
                res.append(path[:])
            
            _myhash = set()
            for i in range(len(temp)):
                
                if temp[i] not in _myhash:
                    _myhash.add(temp[i])
                else:
                    continue
                
                _temp = temp.copy()
                path.append(temp[i])
                _temp.pop(i)
                back_tracking(temp[i], _temp)
                path.pop()
        
        myhash = set()
        for i in range(len(nums)):
            
            if nums[i] not in myhash:
                myhash.add(nums[i])
            else:
                continue
            
            path = [nums[i]]
            temp = nums.copy()
            temp.pop(i)
            back_tracking(nums[i], temp)
            
        return res