# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #rows
        n = len(matrix[0]) #columns


        #figure out row in which the element exists

        l = 0 
        r = m-1

        row_to_search = float("inf")

        while l <= r:
            mid = (l+r)//2

            if matrix[mid][n-1] > target :
                r = mid - 1
                row_to_search = min(mid,row_to_search)
            elif matrix[mid][n-1] < target:
                l = mid + 1
            else:
                return True
        
        if row_to_search == float("inf"):
            return False
        
        #searching the element in row
        l = 0
        r = n-1
        while l<=r :
            mid = (l+r)//2

            if matrix[row_to_search][mid] == target :
                return True
            
            elif matrix[row_to_search][mid] > target :
                r = mid - 1 
            
            else :
                l = mid + 1
        
        return False


# Time Complexity : O(log(m) + log(n))
# Space Complexity : O(1)
    
            