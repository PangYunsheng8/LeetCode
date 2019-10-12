# 方法一：直觉
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         # 如果str为空直接返回0
#         if not str: return 0
        
#         # 去掉所有开头的空格，如果去掉空格后为空，返回0
#         index, length = 0, len(str)
#         while str[index] == ' ' and index < length-1: index += 1
#         if index >= length: return 0
        
#         # 判断正负号
#         isNegative = False
#         if str[index] == '-':
#             isNegative = True
#             index += 1
#         elif str[index] == '+':
#             index += 1
            
#         numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         if index < length:
#             if str[index] in numbers:
#                 res = []
#                 while str[index] in numbers and index < length-1:
#                     res.append(str[index])
#                     index += 1
#                 if str[index] in numbers:
#                     res.append(str[index])
#             else:
#                 return 0
#         else:
#             return 0
        
#         value = int(''.join(res))
#         result = -value if isNegative else value
        
#         if result > pow(2, 31) - 1:
#             return pow(2, 31) - 1
#         if result < -pow(2, 31):
#             return -pow(2, 31)
        
#         return result


# 方法二，主要区别是通过ASCII码判断字符是数字还是字符串
class Solution:
    def myAtoi(self, str: str) -> int:
        # 如果str为空直接返回0
        if not str: return 0
        
        # 去掉所有开头的空格，如果去掉空格后为空，返回0
        index, length = 0, len(str)
        while str[index] == ' ' and index < length-1: index += 1
        if index >= length: return 0
        
        # 判断正负号
        isNegative = 1
        if str[index] == '-':
            isNegative = -1
            index += 1
        elif str[index] == '+':
            index += 1
            
        res = 0
        for i in range(index, length):
            value = ord(str[i])
            if value < 48 or value > 57:
                break
            
            res = res * 10 + (value - 48)
        res = res * isNegative
        
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        
        return res
            
        
        
            
        
        