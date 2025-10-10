# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode() # create a dummy node to get rid of edge cases when we don't yet have an output linked list
        tail = dummynode # store tail to add to the linked list without losing the value of dummynode

        while list1 and list2: # runs until either list is empty
                if list1.val <= list2.val: # if list1 value is less than list2, we add list1's current node to our output list
                    tail.next = list1
                    list1 = list1.next # iterate through the input linked list to only have the next node
                else:
                    tail.next = list2 # same but if list2 value is less 
                    list2 = list2.next
                tail = tail.next # make sure to increment the output list so the next node is the current node for the next iteration
        if list1: # after one of the lists is empty, checks if either list still has elements, if it does, append them to the output list
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummynode.next # return the head value, which is the first node appended to our dummy node.