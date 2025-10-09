class Solution:
    def trap(self, height: List[int]) -> int:
        front, rear = 0, len(height) - 1 # setting up two pointers to iterate over the input array
        maxL = height[front] # two variables to store current maxes for either pointer
        maxR = height[rear]
        res = 0 

        while front < rear: # runs until the pointers cross
            if maxL <= maxR: # checks for the minimum of the pointers' maxes, to ensure water can fit
                front += 1
                maxL = max(maxL, height[front]) # checks if current height is greater than max
                res += maxL - height[front] # if the current height was greater than or equal to the max, zero gets added, otherwise the difference between the heights gets added
            else:
                rear -= 1 # same operations but for the right pointer
                maxR = max(maxR, height[rear])
                res += maxR - height[rear]
        return res # returns the sum of all possible water to store