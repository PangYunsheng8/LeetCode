# class Solution:
#     def combinationSum2(self, candidates, target: int):
#         if not candidates: return []
#         n = len(candidates)
#         candidates = sorted(candidates)
#         path = []
#         res = []
        
#         def dfs(begin, target):
#             if target == 0:
#                 res.append(path[:])
                
#             for index in range(begin, n):
#                 if index > begin and candidates[index] == candidates[index-1]: continue
#                 residue = target - candidates[index]
#                 if residue < 0:
#                     break
#                 path.append(candidates[index])
#                 dfs(index+1, residue)
#                 path.pop()
                
#         dfs(0, target)
#         return res

nums = [1,2,3,4]
nums.pop()
nums.pop()
nums.pop()
print(nums)