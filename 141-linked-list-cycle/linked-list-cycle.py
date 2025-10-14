# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastptr = head # create two pointers, use the tortoise and hare algorithm to determine if a cycle exists
        slowptr = head

        while fastptr and fastptr.next: # runs a while loop until fastptr or fastptr.next is null, which means no cycle exists
            slowptr = slowptr.next # increments the ptrs by 1 and 2 nodes
            fastptr = fastptr.next.next
            if fastptr == slowptr: # if the ptrs meet up then cycle exists since otherwise fastptr should only be ahead of slowptr
                return True
            
        return False # returns true since null was reached by fastptr

