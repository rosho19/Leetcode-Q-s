class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) # set up variables to store the number of columns and rows in 2d matrix
        col = len(matrix[0]) 

        t, b = 0, row - 1 # set up two pointers to run binary search on the rows

        while t <= b: # runs until the target row is found or the pointers cross
            cur = (t + b) // 2
            if target > matrix[cur][-1]:
                t = cur + 1
            elif target < matrix[cur][0]:
                b = cur - 1
            else:
                break

        if not (t <= b): # if the pointers overlapped, then the target row wasn't found so we already know we can't find target
            return False
        
        row = (t + b) // 2 # set up the row that we know the target is in
        l, r = 0, col - 1 # set up two pointers to run binary search on the columns of the row

        while l <= r: # runs until the pointers cross or the target is found
            cur = (l + r) // 2
            if target > matrix[row][cur]:
                l = cur + 1
            elif target < matrix[row][cur]:
                r = cur - 1
            else:
                return True

        return False # return False if the target wasn't in the row