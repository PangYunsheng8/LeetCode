# 两个for循环，相当于暴力法，超时
# class Solution:
#     def minAvailableDuration(self, slots1, slots2, duration: int):
#         slots1 = sorted(slots1)
#         slots2 = sorted(slots2)
#         res = [] 
#         for i in range(len(slots2)):
#             large2 = slots2[i][1]
#             small2 = slots2[i][0]
#             for j in range(len(slots1)):
#                 large1 = slots1[j][1]
#                 small1 = slots1[j][0]
                
#                 if large2 < small1:
#                     break
#                 if small2 > large1:
#                     continue
                
#                 # 判断是否在1的间隔中
#                 if large2 >= small1 and small2 <= large1:
#                     # 求duration
#                     if large2 <= large1 and small2 >= small1:   # 内含
#                         _duration = large2 - small2
#                         if _duration >= duration:
#                             return [small2, small2+duration]
#                     elif large2 >= large1 and small2 <= small1:  # 外包
#                         _duration = large1 - small1
#                         if _duration >= duration:
#                             return [small1, small1+duration]
#                     elif large2 >= large1 and small2 >= small1:  # 右交
#                         _duration = large1 - small2
#                         if _duration >= duration:
#                             return [small2, small2+duration]
#                     elif large2 <= large1 and small2 <= small1:  # 左交
#                         _duration = large2 - small1
#                         if _duration >= duration:
#                             return [small1, small1+duration]
        
#         return []

# 双指针
class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):  #这个判断条件是关键
            if slots2[j][0] < slots1[i][0]:
                if slots1[i][0] + duration <= min(slots2[j][1], slots1[i][1]):
                    return [slots1[i][0], slots1[i][0]+duration]
                j += 1
            else:
                if slots2[j][0] + duration <= min(slots2[j][1], slots1[i][1]):
                    return [slots2[j][0], slots2[j][0]+duration]
                i += 1
        return []
        