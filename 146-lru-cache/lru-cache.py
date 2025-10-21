class Node: # create the class for a doubly linked list node that also stores a key value pair
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int): # initialize the LRUCache with a fields for capacity and the cache that is a hashmap
       self.cap = capacity
       self.cache = {}
       self.left, self.right = Node(0, 0), Node(0, 0) # also set up left and right pointer fields to access most recent and least recently used elements
       self.left.next = self.right
       self.right.prev = self.left
    
    def remove_node(self, node): # removes a node by storing the pointers that point towards the removed node and redirecting to surrounding nodes
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert_node(self, node): # inserts a new pointer to the most recently used spot right before the self.right pointer, adjusts pointers to include new node
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int: # if the key exists, we remove and insert to adjust the node as the most recently used node and return it, otherwise return -1
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None: # if the key exists, we remove it first then insert the new node
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.cap: # if after inserting the node, we overflow the capacity, we remove the least recently used node and also delete it from our cache, so that the length decreases by 1
            lru = self.left.next # set to a variable to keep a copy of the node's key value
            self.remove_node(lru)
            del self.cache[lru.key]