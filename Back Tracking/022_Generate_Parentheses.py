class Solution:
    def generateParenthesis(self, n: int):
        left, right = n, n
        res = []
        item = ''
        
        def back_tracking(left, right, item):
            if left == 0 and right == 0:
                res.append(item)
            
            # 左括号的个数小于n 才能继续放左括号
            if left > 0:
                back_tracking(left-1, right, item+'(')
            
            # 左括号的个数大于右括号的个数才能继续放右括号
            if left < right:
                back_tracking(left, right-1, item+')')
            
        back_tracking(n, n, item)
        return res
            