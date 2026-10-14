class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1 3 1 1 1 4 3 6 9 0 2 4 6 2 10
        
        # 11 8
        
        dq = deque()

        maxes = []
        [1,3,1,2,0,5]
        dq.appendleft(0)
        l = 0
        for r, num in enumerate(nums):
            
            print(dq)
            while dq and (num > nums[dq[-1]] or dq[-1] < l):
                dq.pop()

            while dq and (num > nums[dq[0]]):
                dq.popleft()

            dq.appendleft(r)
            print(dq, 'after')


            if r - l + 1 == k:
                maxes.append(nums[dq[-1]])
                print('added', nums[dq[-1]], l, r)
                l+=1

        return maxes

        