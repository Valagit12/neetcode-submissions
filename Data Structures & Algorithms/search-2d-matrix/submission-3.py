class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(target):
            low = 0
            high = len(matrix) - 1

            mid = (low + high) // 2

            while low <= high:
                mid = (low + high) // 2

                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][0] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return mid
            
        
        def binarySearch2(target, lis):
            low = 0
            high = len(lis) - 1

            mid = (low + high) // 2
            while low <= high:
                mid = (low + high) // 2

                if lis[mid] == target:
                    return mid
                elif lis[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return mid

        mid = binarySearch(target)
        final = binarySearch2(target, matrix[mid])
        print(matrix[mid][final])
        return matrix[mid][final] == target

        
        