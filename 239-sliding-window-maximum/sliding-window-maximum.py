class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [] # output array for storing the solution
        queue = collections.deque() # using a deque to be able pop numbers from either side and have a decreasing stack structure, storing indices to easily recognize if elements are in the window
        l = 0 # left pointer

        for r in range(len(nums)): # loop that runs the right pointer through the input array
            while queue and nums[queue[-1]] < nums[r]: # if queue is non empty and the right most value(lowest value) is less than new value then we pop to maintain decreasing stack
                queue.pop()
            queue.append(r)

            if l > queue[0]: # removes values that are out of window scope as left pointer increments, in our queue that means only the current maximum values get removed
                queue.popleft()
            
            if (r + 1) >= k: # for the first k iterations, we don't append elements to result output array and keep left pointer stationary
                result.append(nums[queue[0]])
                l += 1
                
        return result # return output array