class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefixarray = [-1 for _ in range(len(nums))]
        suffixarray = [-1 for _ in range(len(nums))]
        prefix = 0
        suffix = 0
        res = nums[0]
        for i in range(len(nums)):
            prefixarray[i] = (prefix or 1) * nums[i]
            suffixarray[len(nums) - i - 1] = (suffix or 1) * nums[-1 - i]
            prefix = prefixarray[i]
            suffix = suffixarray[-1 - i]
            res = max(res, prefix, suffix)

        print(suffixarray)

        return res





                 
