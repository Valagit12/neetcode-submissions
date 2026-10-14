import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums))]

        for num in freq:
            bucket_idx = freq[num] - 1

            buckets[bucket_idx].append(num)
        
        ans = []

        for bucket in reversed(buckets):
            for elem in bucket:
                ans.append(elem)
                k -= 1
            if k == 0:
                break

        return ans
        
        



