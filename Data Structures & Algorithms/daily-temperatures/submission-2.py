class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = temperatures[0:]
        temp.reverse()

        stack = []
        ans = []

        stack.append(len(temperatures) - 1)
        ans.append(0)
        

        for i in range(len(temperatures)-2, -1, -1):
            num = temperatures[i]
            while stack and temperatures[stack[-1]] <= num:
                stack.pop()
            
            if not stack: ans.append(0)
            else: 
                print(stack[-1] - i, stack, i)
                ans.append(stack[-1] - i)

            stack.append(i)
            
        ans.reverse()
        return ans
