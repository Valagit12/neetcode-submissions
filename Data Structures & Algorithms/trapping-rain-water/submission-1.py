class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        potential = 2
        total = 9
        length = 3
        '''
        if not height:
            return 0

        left = 0
        right = len(height)-1

        maxLeft = height[left]
        maxRight = height[right]

        answer = 0
        while left < right:

            if maxLeft <= maxRight:
                left+=1
                maxLeft = max(height[left], maxLeft)
                answer += maxLeft - height[left]
            elif maxRight < maxLeft:
                right-=1
                maxRight = max(height[right], maxRight)
                answer += maxRight - height[right]
        
        return answer






        
        
        