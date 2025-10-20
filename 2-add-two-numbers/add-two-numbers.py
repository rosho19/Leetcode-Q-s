# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # when returning a list, easier to create a dummy node to remove edge cases when first inserting a node
        cur = dummy # sets up a pointer to iterate through our new list

        carry = 0 # initializes carry variable to help compute the addition
        while l1 or l2 or carry: # runs a loop until both input lists are empty, and if the carry is 0, which covers the edge case that the final two digits of both lists have a leftover carry
            d1 = l1.val if l1 else 0 # initializes the current digit of either list, or sets it to 0 if the list has ended
            d2 = l2.val if l2 else 0

            val = d1 + d2 + carry # computes the addition with the carry

            carry = val // 10 # adjusts the carry value to 1 or 0 if the value is greater than 10
            val = val % 10 # adjusts the val so we only get the single digit from the addition

            cur.next = ListNode(val) # increments the cur pointer while initializing a new node in our new linked list
            cur = cur.next

            l1 = l1.next if l1 else None # increments the two list pointers if it is currently not null, otherwise it keeps it at null 
            l2 = l2.next if l2 else None
        
        return dummy.next # returns the new list excluding the dummy node 

