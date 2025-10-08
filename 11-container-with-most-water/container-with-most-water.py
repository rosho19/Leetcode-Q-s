class Solution:
    def maxArea(self, height: List[int]) -> int:
        curmax = 0 # to keep track of the running max 
        front = 0 # setting up two pointers as we iterate through the input array
        rear = len(height) - 1

        while front < rear: # run a loop until the two pointers cross
            curmax = max(curmax, ((rear - front) * min(height[front], height[rear]))) # check if the current area is larger than the current max
            if height[front] <= height[rear]: # move the pointer with the lowest height, since the lowest height determines the length of the area
                front += 1
            else:
                rear -= 1
    
        return curmax # returns our max area throughout the array