class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        previous = None

        ans = set()
        for i, to_skip in enumerate(nums):
            if previous == to_skip:
                continue
            previous = to_skip
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue

                summ = (nums[left] + nums[right])
                if summ < -1*to_skip:
                    left += 1
                elif summ > -1*to_skip:
                    right -= 1
                else:
                    ans.add(tuple(sorted((nums[left], to_skip, nums[right]))))
                    left += 1
                    right -= 1
                    continue
        
        return [list(sett) for sett in ans]
            
    # -4 -1 -1 0 1 2