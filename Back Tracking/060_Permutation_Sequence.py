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

def frac(n):
    if n == 0: return 0
    res = 1
    temp = n
    while temp > 0:
        res *= temp
        temp -= 1
    return res

a = frac(0)
print(a)