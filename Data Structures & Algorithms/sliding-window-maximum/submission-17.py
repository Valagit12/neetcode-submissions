class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        l = 0
        for r, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if r >= k - 1:
                print(dq[0])
                ans.append(nums[dq[0]])
                l+=1
        
        return ans

        