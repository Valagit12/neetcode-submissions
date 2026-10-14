class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = -1, len(A) - 1

        '''
        0 1 2 3 4 5 6 7 8 9 10
        half = 5
        i = 2
        B 0 1 5 6 9 10
        A 2 3 4 7 8

        '''
        while l <= r:
            i = (l + r) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float('-inf')
            rightA = A[i + 1] if i + 1 < len(A) else float('inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightB = B[j + 1] if j + 1 < len(B) else float('inf')

            print(f"l: {l} | r: {r} | leftA : {leftA} | rightA : {rightA} | leftB : {leftB} | rightB : {rightB} | i : {i} | j : {j}")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) +  min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
        return -1
            









  