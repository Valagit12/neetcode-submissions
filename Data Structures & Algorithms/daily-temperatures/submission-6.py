class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        

        stack = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if len(stack) > 0:
                output[i] = stack[-1] - i
            
            stack.append(i)
                
            
        
        return output


'''
30: 38, 30 36 35 40 28
38: 40, 28 
30: 36i, 40i -> [3, 5] head is greater, compute using index length, append to stack, move on
36: 40 -> [4, 5] head is not greater, pop from stack until greater. head is greater, compute using index length, append to stack, move on
35: 40i -> [5] head is greater, compute using index length, append to stack, move on
40: [] -> [6] head is not greater, pop from stack until greater. stack is empty, append to stack, move on
28: [] -> stack is empty, append to stack, move on

'''