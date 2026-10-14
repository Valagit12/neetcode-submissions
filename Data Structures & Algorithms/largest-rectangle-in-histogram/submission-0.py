class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, num in enumerate(heights):
            
            start = i
            while stack and stack[-1][1] > num:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, num))
        
        for i, num in stack:
            maxArea = max(maxArea, num * (len(heights) - i))
        
        return maxArea


        