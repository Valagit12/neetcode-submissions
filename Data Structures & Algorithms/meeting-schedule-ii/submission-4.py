"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        dic = defaultdict(int)

        for interval in intervals:
            start, end = interval.start, interval.end
            dic[start] += 1
            dic[end] -= 1

        maxmeetingCount = 0
        currmeetingCount = 0
        for i in sorted(dic):
            currmeetingCount += dic[i]
            maxmeetingCount = max(maxmeetingCount, currmeetingCount)
        
        return maxmeetingCount
        

        