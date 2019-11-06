class Solution:
    def merge(self, intervals):
        if not intervals: return []
        
        # 排序
        intervals.sort()
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # 如果可以合并，合并插入
            if intervals[i][0] <= res[-1][1]:
                if res[-1][1] < intervals[i][1]: res[-1][1] = intervals[i][1]
            # 如果不能合并，直接插入
            else: res.append(intervals[i])
        
        return res