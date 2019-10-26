# 方法一：正常回溯，算法给出的结果是没问题的，但是用回溯会超时
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         res = [] 
#         path = []
        
#         def back_tracking():
#             if len(path) >= n:
#                 res.append(path[:])
#                 return
            
#             for i in range(1, n+1):
#                 if i in path:
#                     continue
#                 if len(res) == k:
#                     break
#                 path.append(i)
#                 back_tracking()
#                 path.pop()
                
#         back_tracking()
#         return ''.join([str(i) for i in res[k-1]])

# 方法二：回溯+剪枝
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1: return "1"
        path = []
        
        def frac(n):
            if n == 0: return 0
            res = 1
            temp = n
            while temp > 0:
                res *= temp
                temp -= 1
            return res
        
        def back_tracking(level, temp_k):
            for i in range(1, n+1):
                if i in path:
                    continue
                
                value = frac(n-level)
                if value == 0:
                    path.append(i)
                    return 
                
                if temp_k > value:
                    temp_k = temp_k - value
                    continue
                
                path.append(i)
                back_tracking(len(path)+1, temp_k)
                
        back_tracking(1, k)
        return ''.join([str(i) for i in path])