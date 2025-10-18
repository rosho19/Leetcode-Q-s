"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
        

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curnode = head # set a variable to iterate through the list
        nodes = {None : None} # initialize a hashmap where Null values are set to Null

        while curnode: # first pass through the list, we just copy all nodes in the list to the hashmap
            copy = Node(curnode.val)
            nodes[curnode] = copy
            curnode = curnode.next
        
        curnode = head # reset variable to head
        while curnode: # second pass through the list, we take the value, next and random values of each node and set it to copy
            copy = nodes[curnode]
            copy.next = nodes[curnode.next]
            copy.random = nodes[curnode.random]
            curnode = curnode.next
        return nodes[head] # return the head of the hashset which contains the new linked list