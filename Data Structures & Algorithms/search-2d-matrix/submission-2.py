class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows, ncols = len(matrix), len(matrix[0])
        first_row, last_row = 0, nrows-1   

        while first_row <= last_row:
            m = (first_row +last_row)//2   

            if target > matrix[m][-1]:
                first_row = m+1
            
            elif target < matrix[m][0]:
                last_row = m -1
            
            else:
                break
        
        if not (first_row<=last_row):
            return False
            
        l,r = 0, len(matrix[m])
        while l<=r:
            mid = (l+r)//2
            if target == matrix[m][mid]:
                return True
            elif target > matrix[m][mid]:
                l = mid + 1
            else:
                r = mid -1
        
        return False