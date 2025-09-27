class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       col = [0] * 9
       row = [0] * 9
       square = [0] * 9 # making the arrays for columns, rows, and square to figure out coordinates

       for r in range(9):
        for c in range(9):
            if board[r][c] != ".": #iterates over the board until it reaches a number
                val = int(board[r][c]) - 1 # finds the index we want to bitmask "val"
                if (1 << val) & row[r]: # if when "val" is bitmasked and row[r] already stores the same value, then we return false since that number already exists
                    return False
                if (1 << val) & col[c]: # same as above
                    return False
                if (1 << val) & square[(r // 3) * 3 + (c // 3)]: # similar logic, but we use a formula to find the correct square
                    return False
                
                row[r] |= (1 << val) # since the number doesn't break any rules, we add it to the right coordinate use bitwise OR operator
                col[c] |= (1 << val)
                square[(r // 3) * 3 + (c // 3)] |= (1 << val)
       return True  