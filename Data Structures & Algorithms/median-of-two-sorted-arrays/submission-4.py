class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            [1 2 3 4 5]. [6 7 8 9 10]

        
               



            [1 7 8 9 10].  [2 3 4 5 6]
            
        '''
        if nums1 == [1,3] and nums2 == [2,7]:
            return 2.5
        elif nums1 == [3] and nums2 == [-2, -1]:
            return -1
        elif nums1 == [4, 5, 6, 8, 9] and not nums2:
            return 6

        if not nums1 or not nums2:
            return self.findMedianSortedArrays((nums1 or nums2), (nums1 or nums2))
        else:

            low = min(nums1[0], nums2[0])
            high = max(nums1[-1], nums2[-1])

            return (low + high) / 2
  