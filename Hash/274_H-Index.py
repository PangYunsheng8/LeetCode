class Solution:
    def hIndex(self, citations) -> int:
        h = 0
        citations = sorted(citations)[::-1]
        for i in range(len(citations)):
            h = i + 1
            if citations[i] < h: return h-1
        return h 