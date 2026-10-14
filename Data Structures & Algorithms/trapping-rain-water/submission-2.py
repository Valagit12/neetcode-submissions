class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        if len(height) <= 2:
            return ans
        
        left, right = 0, len(height) - 1

        maxLeft, maxRight = height[left], height[right]


        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]

            if leftHeight <= rightHeight:
                ans += min(maxLeft, maxRight) - leftHeight
                left+=1
                maxLeft = max(maxLeft, height[left])
            else:
                ans += min(maxRight, maxLeft) - rightHeight
                right-=1
                maxRight = max(maxRight, height[right])
        
        return ans




        
        
        