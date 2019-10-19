class Solution:
    def missingNumber(self, arr) -> int:
        sub1 = arr[1] - arr[0]
        sub2 = arr[2] - arr[1]
        if abs(sub2) >= abs(sub1):
            true_sub = sub1
        else:
            true_sub = sub2
        
        for i in range(1, len(arr)):
            _sub = arr[i] - arr[i-1]
            if _sub != true_sub:
                return arr[i] - true_sub
        return 0
        
            