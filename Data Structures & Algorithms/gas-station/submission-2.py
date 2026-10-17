class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        currGas = 0
        curr = 0

        '''
        [1,2,3] [2 3 2]
        start 2
        currgas 0
        curr 2
        '''
        for _ in range(2 * len(gas)):
            currGas += gas[curr] - cost[curr]

            if currGas < 0:
                if start == len(gas) - 1:
                    return -1
                currGas = 0
                if curr == len(gas) - 1:
                    curr = 0
                else:
                    curr = curr + 1
                start = curr
                continue
            
            if curr == len(gas) - 1:
                curr = 0
            else:
                curr = curr + 1

            if curr == start:
                return start
                
        return -1
            

