class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        res = [intervals[0]]
        it = iter(intervals)
        first = next(it)
        prevEnd = first[1]

        for interval in it:
            if interval[0] <= prevEnd:
                res[-1][1] = max(interval[1], prevEnd)
                prevEnd = res[-1][1]
            else:
                res.append(interval)
                prevEnd = interval[1]
        
        return res


        
        