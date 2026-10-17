class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        xyxxyzbzbbisl

        x 0, 3
        y 1, 4
        z 5, 7
        b 6, 9 
        i 10, 10
        s 11, 11
        l 12, 12

        (0, 3) (1, 4)

        ans = []
        prevStart = 0
        prevEnd = 3
        for i, j in each interval[1:]
            i < prevEnd:
                prevEnd = j
            if i == prevEnd:
                never should happen
            if i > prevEnd:
                ans.append(prevEnd - prevStart)
                prevStart = i,
                prevEnd = j
        '''
        intervals = {}
        # intervals: {x: (0, 1), y: (0, 0), }
        for i in range(len(s)):
            char = s[i]
            if char not in intervals:
                intervals[char] = (i, i)
            else:
                intervals[char] = (intervals[char][0], i)
        print(intervals)
        intervals = list(intervals.values())
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        ans = []
        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = max(end, prevEnd)
            elif i == prevEnd:
                return False
            elif i > prevEnd:
                ans.append(prevEnd - prevStart + 1)
                prevStart = start
                prevEnd = end
        ans.append(prevEnd - prevStart + 1)
        
        return ans

        