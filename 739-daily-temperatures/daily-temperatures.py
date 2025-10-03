class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = len(temperatures) * [0]
        stack = [] # set up stack with index and value for each element

        for i, n in enumerate(temperatures): #check both index and temp of each element
            while stack and n > stack[-1][0]: # takes the top of the stack and checks the temp
                stackT, stackInd = stack.pop() # we pop if the stack isn't empty and the current value is greater than the value stored at the top of the stack # the variables hold the two values from the popped stack element
                result[stackInd] = i - stackInd # sets the output as the current index minus the popped element's index
            stack.append([n, i]) # appends the current value to then find a bigger value if available        
        return result    