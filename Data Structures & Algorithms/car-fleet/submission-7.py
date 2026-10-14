class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # [a b 0 0 c 0 0 d 0 0 0]

        '''

        10 - 4 = 6 / 2 = 3

        10 - 1 = 9 /2 = 5

        10 - 0 = 10 / 1 = 10
        
        10 - -1 = 11 / 5 = 3

        10 - 7 = 3 / 1 = 3

        '''

        turns_take = []
        for i in range(len(position)):
            turns_take.append((target - position[i])/speed[i])
        
        pair = [(p,s,t) for p, s, t in zip(position, speed, turns_take)]
        pair_sorted = sorted(pair)
        pair_sorted.reverse()

        print(pair_sorted)

        stack = []
        for p, s, t in pair_sorted:
            if (stack and stack[-1] >= t):
                continue
            else:
                stack.append(t)
        

        return len(stack)







            
        