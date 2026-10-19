class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        prevEnd = intervals[0][1]

        ans = 0
        ansFlag = False
        for i in range(1, len(intervals)):
            # print(intervals[i], prevEnd)
            if intervals[i][0] < prevEnd:
                ans+=1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
        
        return ans