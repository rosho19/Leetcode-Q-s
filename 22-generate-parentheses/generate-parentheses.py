class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ["("]
        result = []

        def add_parenth(leftp, rightp): # helper function to check 3 conditions 
            if leftp == rightp == n: # first condition, base case for when we have n open and close parentheses, which make up n pairs
                result.append("".join(stack)) # appends the results of each substring from stack to result
                return # since it's a helper fcn, there's no need to return anything

            if leftp < n: # second condition, checks if there are less than n open parentheses
                stack.append("(")
                add_parenth(leftp + 1, rightp)
                stack.pop() # removes the extra parentheses since we only use one stack to store all cases. 

            if rightp < leftp: # third condition, ensures there are less closing parentheses than open before adding another closing one.
                stack.append(")")
                add_parenth(leftp, rightp + 1)
                stack.pop()

        add_parenth(1, 0) # runs the function starting with the open parentheses since that's the only starting choice
        return result