# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # since we adjust the head of the list, we use dummy node 
        prevgrp = dummy # use a previous group pointer to keep track of where the previous k group was

        while True: # runs until there are no more multiples of k nodes left in the list
            count = 0
            temp = prevgrp
            while temp and count < k: # increments a temp pointer k times 
                temp = temp.next
                count += 1
            if not temp: # if temp is Null, then we break since we've reached the end of the list
                break
            nextgrp = temp.next # we set the next group pointer since the node after the kth node is a new group

            prev, cur = temp.next, prevgrp.next # we set prev as this so that in the first iteration of the following loop, the next pointer of cur is the next group
            while cur != nextgrp: # runs until we reach the next k group, classis linked list reversal
                temp2 = cur.next
                cur.next = prev
                prev = cur
                cur = temp2
            temp2 = prevgrp.next # stores the pointer to the start of this k group
            prevgrp.next = temp # adjusts what the new start of the k group should be 
            prevgrp = temp2 # after reversal the start of the k group is now the end of the group
        return dummy.next # returns head.     