# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastptr = head # create two pointers, use the tortoise and hare algorithm to determine if a cycle exists
        slowptr = head
        if slowptr and slowptr.next: # sets up base case where if index 0-2 is null, then no cycle exists. If cycle exists, null should never be found
            slowptr = slowptr.next
            if slowptr.next:
                fastptr = slowptr.next
            else: 
                return False
        else:
            return False

        while fastptr: # runs a while loop until fastptr is null, which means no cycle exists
            if fastptr == slowptr: # if the ptrs meet up then cycle exists since otherwise fastptr should only be ahead of slowptr
                return True
            if not (fastptr.next and fastptr.next.next): # checks if the fastptr reaches null before we increment it
                return False
            slowptr = slowptr.next # increments the ptrs by 1 and 2 nodes
            fastptr = fastptr.next.next
        return False # returns true since null was reached by fastptr
