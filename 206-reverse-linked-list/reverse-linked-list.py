# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curnode = head # maintains the current node and previous node while iterating through linked list
        prevnode = None
        while curnode: # runs until the current node is null (previous node pointed to null)
            temp = curnode.next # stores the next node to not lose the rest of the linked list
            curnode.next = prevnode # points to the previous node instead
            prevnode = curnode # increments the previous node to the current for the next iteration
            curnode = temp # increments the current node to the next node for the next iteration
        return prevnode # returns what is the new head, since the current node when the while loop fails is null