# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # create a dummy node to have index 1 be the head
        first, second = dummy, dummy # set two pointers to run a greedy algorithm approach

        for i in range(n): # iterate first pointer n steps so that we create a distance of n nodes between the two pointers
            first = first.next

        while first.next: # increment both pointers right before first is null, where the second pointer is just before the node that needs to be removed
            first = first.next
            second = second.next

        second.next = second.next.next  # we remove the node by setting the second nodes next to the node after the one being removed.
        return dummy.next # return head
        