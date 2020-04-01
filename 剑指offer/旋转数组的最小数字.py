# 分治算法, 时间复杂度O(logN), 空间复杂度O(1)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]: left = mid + 1
            elif numbers[mid] < numbers[right]: right = mid
            else: right -= 1

        return numbers[left]

        