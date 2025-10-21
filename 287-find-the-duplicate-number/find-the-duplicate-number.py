class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 # use the tortoise and hare algorithm using two pointers to identify a cycle, which we know will occur

        while True: # runs until the fast pointer eventually reaches the slow pointer due to a cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0 # create a new pointer to identify the start of the cycle

        while True: # runs until this new pointer and slow pointer reach the same value, which we know will happen since both pointers are the same distance away from the start of the cycle.
            slow = nums[slow] # iterating both pointers by 1 step ensures they both reach the duplicate number
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow # return either pointer to get the necessary number