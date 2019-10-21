class Solution:
    def permute(self, nums):
        res = []
        
        def back_tracking(num, temp):
            if not temp:
                res.append(path[:])
            else:    
                for index in range(len(temp)):
                    path.append(temp[index])
                    _temp = temp.copy()
                    _temp.pop(index)
                    back_tracking(temp[index], _temp)
                    path.pop()
        
        for i in range(len(nums)):
            path = [nums[i]]
            temp = nums.copy()
            temp.pop(i)
            back_tracking(nums[i], temp)
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    results = solution.permute(nums)
    print(results)
                
            