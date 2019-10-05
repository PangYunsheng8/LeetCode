class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height) - 1 
        maxCol = 0
        while low <= high:
            col = min(height[low], height[high]) * (high-low)
            if col > maxCol:
                maxCol = col
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxCol