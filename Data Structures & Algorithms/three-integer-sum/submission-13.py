class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        previous = None
        ans = []
        for i, to_skip in enumerate(nums):
            if previous == to_skip:
                continue
            previous = to_skip
            left = i+1
            right = len(nums) - 1
            while left < right:
                if left == i :
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue

                summ = (nums[left] + nums[right])

                print(nums[left], nums[right], to_skip)
                if summ < -1*to_skip:
                    left += 1
                elif summ > -1*to_skip:
                    right -= 1
                else:
                    ans.append([nums[left], to_skip, nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                    continue
        
        return ans
            
    # -4 -1 -1 0 1 2