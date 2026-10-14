class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []




        l = 0
        for r in range(len(nums)):
            rnum = nums[r]
            while dq and nums[dq[0]] < rnum:
                dq.popleft()
            dq.appendleft(r)
            
            if r >= k and dq[-1] < l:
                dq.pop()
            
            if r >= k-1:
                ans.append(nums[dq[-1]])
                l+=1
        
        return ans










        

        