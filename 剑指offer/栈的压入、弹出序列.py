# 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx_push = 0
        for i in range(len(popped)):
            num = popped[i]
            if stack and stack[-1] == num: 
                stack.pop() 
            else:
                while idx_push < len(pushed):
                    stack.append(pushed[idx_push])
                    idx_push += 1
                    if pushed[idx_push-1] == num: break
                if stack and stack[-1] == num: 
                    stack.pop()
                else: return False
        return True