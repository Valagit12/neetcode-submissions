class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for key in hashmap:
            if hashmap[key] == 1:
                return key
        