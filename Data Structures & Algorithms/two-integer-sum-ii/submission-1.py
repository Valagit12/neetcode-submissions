class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            lown = numbers[low]
            highn = numbers[high]

            if lown + highn < target:
                low += 1
            elif lown + highn > target:
                high -= 1
            else:
                return [low + 1, high + 1]
