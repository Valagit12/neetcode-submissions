class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Because the intervals are coming in order, and the solution requires some form of searching, we can do binary search
        # First binary search for the position of newInterval
        if not intervals:
            return [newInterval]

        left = 0
        right = len(intervals) - 1
        # We will use the first elements to do the binary search, and insert newInterval right before when it is most valid based on the starting intervals.
        target = newInterval[0]

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            elif intervals[mid][0] >= target:
                right = mid - 1
        # When the binary search ends, left = right + 1. 
        # Every element less than left will be less than target and equal to and greater than left will be greater than target
        intervals.insert(left, newInterval)


        # Now, we are guaranteed to have at most one interval that needs to merge with others.
        # We will traverse the intervals array until we detect it
        prevStart, prevEnd = intervals[0]
        res = [[prevStart, prevEnd]]
        for start, end in intervals[1:]:
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
                prevEnd = res[-1][1]
            else:
                res.append([start, end])
                prevStart = start
                prevEnd = end
        
        return res          
