class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = deque()

        for r in range(len(temperatures)-1, -1, -1):
            num = temperatures[r]
            while stack and temperatures[stack[-1]] <= num:
                stack.pop()

            if not stack:
                ans.appendleft(0)
            else:
                ans.appendleft(stack[-1] - r)

            stack.append(r)   
        
        return list(ans)
            

        