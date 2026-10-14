class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[high] == target:
                return high
            elif nums[low] == target:
                return low

            elif nums[mid] <= nums[high]:
                
                if target < nums[mid] or nums[high] < target:
                    high = mid - 1
                else:
                    low = mid + 1

            else: #  2 3 4 5 6 7 1, 3 4 5 1 2,
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1