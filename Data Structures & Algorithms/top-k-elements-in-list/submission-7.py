import heapq

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     frequencies = {}

    #     for num in nums:
    #         frequencies[num] = frequencies.get(num, 0) + 1
        
    #     heap = []
    #     for bucket in frequencies.keys():
    #         heapq.heappush(heap, (-frequencies[bucket], bucket))


    #     ans = []
    #     for i in range(k):
    #         ans.append(heapq.heappop(heap)[1])
        
    #     return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        buckets = [[] for i in range(len(nums) + 1)]

        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        for bucket in frequencies.keys():
            buckets[frequencies[bucket]].append(bucket)
        
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        



