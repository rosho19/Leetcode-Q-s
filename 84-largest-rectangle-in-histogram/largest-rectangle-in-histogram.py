class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # storing both index and height of bars
        maxarea = 0 # storing current max area found

        for i, h in enumerate(heights):
            start = i # assuming the rectangle moves to the right starting from here
            while stack and h < stack[-1][1]: # checks if the stack isn't empty and if the current height is less than the top of the stack's height
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index)) # calculated the width by finding the difference between current index and index of popped rectangle
                start = index # since the height from the top of the stack was greater than current, we can set the start back
            stack.append((start, h)) # now we append the current bar's height and the start index that we found based on how many bars before it were taller

        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i)) # since these bars were extended to the end of the stack, widht is the difference from index to the entire length of array

        return maxarea