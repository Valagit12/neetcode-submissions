class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # matrix = [[1], [5], [8], [10], [11], [12], [15], [20], [31]]
        # target = -2

        # log m * n =log m + log n

        ## find the row
        l = 0
        r = len(matrix) - 1
        mid = (l + r) / 2
        while l < r:
            mid = ((l + r + 1) // 2)
            midvalue = matrix[mid][0]
            lvalue = matrix[l][0]
            rvalue = matrix[r][0]
            
            if midvalue == target:
                return True

            if midvalue > target:
                if lvalue <= target:
                    mid = l
                    break
                r = mid - 1
            else:
                l = mid

        l = 0
        r = len(matrix[0]) - 1
        row = int(mid)
        while l <= r:
            mid = (l + r) // 2
            midvalue = matrix[row][mid]
            lvalue = matrix[row][l]
            rvalue = matrix[row][r]

            if midvalue == target:
                return True
            elif midvalue < target:
                l = mid + 1
            else:
                r = mid - 1        
        
        return False


        ## find the column

