class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Each container is 1 unit apart

        Want to maximize sum of height and length
        '''

        maxArea = 0

        left = 0
        right = len(heights) - 1
        n = right + 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            maxArea = max(maxArea, height*width)

            if height == heights[left]:
                left+=1
            else:
                right-=1
        
        return maxArea
        