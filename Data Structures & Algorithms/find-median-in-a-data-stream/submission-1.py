'''
MedianFinder is an object

addNum adds an integer to a data stream

findMedian returns the median of all elements so far

'''

'''
minheap

1 3 5 7  9 10

        1
    3.    5
7.  9.  10

        
        10
    9       5
7       3 1   
              

'''



class MedianFinder:

    def __init__(self):
        self.largeheap = [] #minheap
        self.smallheap = [] # maxheap
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap, -1 * num)      

        if (self.largeheap and self.smallheap and -1*self.smallheap[0] > self.largeheap[0]):
            val = -1 * heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, val)
        
        if len(self.smallheap) > len(self.largeheap) + 1:
            val = -1 * heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, val)
        
        if len(self.largeheap) > len(self.smallheap) + 1:
            val = -1 * heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap, val)

    def findMedian(self) -> float:
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        elif len(self.smallheap) > len(self.largeheap):
            return -1*self.smallheap[0]
        else:
            return (self.largeheap[0] + -1*self.smallheap[0]) / 2

        
        
        