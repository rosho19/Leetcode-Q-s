# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: # base cases for null input list
            return None
        
        while len(lists) > 1: # the length of the input lists will keep decreasing as the lists continue to get merged into fewer distinct lists
            merged = [] # create temporary variable to store the results of the merge2lists helper function

            for i in range(0, len(lists), 2): # runs a for loop incremented by 2 to cover the 2 lists being merged each time
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # ensures that in the case the k lists is odd, i + 1 won't be out of bounds
                merged.append(self.merge2lists(l1, l2)) # continously appends the result of the merged lists, where only the most recent result is the one that matters
            lists = merged
        return lists[0] # that's why we print the first value of lists
    

    def merge2lists(self, list1, list2):
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
        