# 方法一：直觉，写起来很麻烦
# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         res = []
#         mysta = {1:"I", 5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
#         for index, number in enumerate(str(num)[::-1]):
#             number = int(number)
#             _res = ""
#             if number < 4 and number > 0:
#                 _res = mysta[pow(10, index)] * number
#             elif number == 4:
#                 _res = mysta[pow(10, index)] + mysta[pow(10, index)*5]
#             elif number > 4 and number < 9:
#                 _res = mysta[pow(10, index)*5] + mysta[pow(10, index)] * (number -5)
#             elif number == 9:
#                 _res = mysta[pow(10, index)] + mysta[pow(10, index+1)]
#             res.append(_res)
#         return "".join(res[::-1])

# 方法二：贪心算法
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        index = 0
        res = ""
        while index < 13:
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res
                