class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        
        index = 0
        number = 0
        while index < len(s) - 1:
            if s[index:index+2] in romans.keys():
                number += romans[s[index:index+2]]
                index += 2
            else:
                number += romans[s[index:index+1]]
                index += 1
        if len(s) == 1:
            return romans[s]
        elif s[-2:] in romans:    
            return number
        else:
            return number+romans[s[-1]]
                
            