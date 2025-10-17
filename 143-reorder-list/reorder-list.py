# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next # create fast and slow pointers to find the middle of the array
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        l2 = slow.next # set the start of the second list
        slow.next = None # separates first list from second 
        prev = None # initalizes prev to reverse second list
        while l2: # reverses the second list
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l1 = head # sets the start for both lists
        l2 = prev  

        while l2: # appends the two lists based on the problem's requirements
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp
            l1 = temp
            l2 = temp2 