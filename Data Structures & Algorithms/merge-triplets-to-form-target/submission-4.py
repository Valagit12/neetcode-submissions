class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundElementsOfTarget = [-1, -1, -1]

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    foundElementsOfTarget[i] = target[i]
            
        
        return target == foundElementsOfTarget
            

        