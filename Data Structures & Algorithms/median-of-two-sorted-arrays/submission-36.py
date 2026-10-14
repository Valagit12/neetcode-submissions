class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        #A is the smaller list
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l = -1
        h = len(A) - 1

        while l <= h:
            midA = (l + h) // 2
            midB = half - midA - 2

            leftA = A[midA] if midA >= 0 else float('-inf')
            rightA = A[midA + 1] if midA + 1 < len(A) else float('inf')
            leftB = B[midB] if midB >= 0 else float('-inf')
            rightB = B[midB + 1] if midB + 1 < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                return min(rightA, rightB)

            elif leftA > rightB:
                h = h - 1

            else:
                l = l + 1
            


        

        # 1 3

        # 2 4



        
        # 1 1 3 4 5

        # 1, 3, 5

        # 1, 2



            









  