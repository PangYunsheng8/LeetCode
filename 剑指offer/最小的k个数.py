# 方法一: 快排，时间复杂度O(n),空间复杂度O(logn)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): return arr
        return self.quick_select(arr, 0, len(arr)-1, k)

    def partition(self, arr, left, right):
        v = arr[left]
        while left < right:
            while left < right and arr[right] >= v: right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= v: left += 1
            arr[right] = arr[left]
        arr[left] = v
        return left

    def quick_select(self, arr, left, right, k):
        p = self.partition(arr, left, right)
        if p == k: return arr[:k]
        elif p < k: return self.quick_select(arr, p+1, right, k)
        elif p > k: return self.quick_select(arr, left, p-1, k)


# 方法二：最大堆，时间复杂度O(nlogk),空间复杂度O(k)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans