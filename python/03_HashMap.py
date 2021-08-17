# =================================================================== #
# Hash Map                                                            #
#                                                                     #
# Operations:                                                         #
# Lookup O(1) (but it can be O(n) if poor hash function is chosen)    #
# Insertion, removal O(1)                                             #     
#                                                                     #
# Collisions are handled with linked lists here for faster lookups.   #
# A simpler alternative would be to use arrays instead                #
# Another data structure used in combination with chaining is         #
# the binary search tree, which has a worst case guarantee for        #
# searching, and insertion of logn.                                   #
#                                                                     #
# Improvements:                                                       #
# 1. Increase size of underlying array based on load factor           # 
#                                                                     #
#               load_factor = num_elements / num_buckets              #
# 2. Use a binary tree to handle collisions in the buckets.           # 
# =================================================================== #

class MyHashMap:

    def __init__(self):
        """
        Initialize with number of buckets. A better choice is a prime 
        number. With growing size of the hashmap the number of buckets
        could be increased based on the load factor.
        """
        self.num_buckets = 1000
        self.data = [LinkedList() for x in range(self.num_buckets)]

    def put(self, key, value):
        """
        Adds a <key, val> pair to hashmap. Here it is val >= 0.
        """
        index = self.hash(key)
        self.data[index].add_tail(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.
        """
        index = self.hash(key)
        val = self.data[index].search_val(key) 
        return val
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this 
        map contains a mapping for the key.
        """
        index = self.hash(key)
        self.data[index].remove_key(key)
        
    def hash(self, key):
        """
        Hash function to map key -> index.
        """
        index = key % self.num_buckets
        return index


class Node:
    def __init__(self, key, val, next_node=None):
        """
        Stores both a key and a val.
        """
        self.key = key
        self.val = val
        self.next = next_node

     
class LinkedList:
    def __init__(self):
        """
        Initialized with an empty node None for easier handling 
        of data nodes.
        """
        self.size = 0
        self.head = Node(None, None) # Dummy node
    
    def add_tail(self, key, val):
        """
        Adds a node at the end of the list.In some cases it 
        can be faster to add at the head instead.
        """
        if self.search_val(key) is not -1:
            self.remove_key(key)        
        
        new_node = Node(key, val)
        pred = self.head   
        while pred.next is not None:
            if pred.next.val is val:
                return
            pred = pred.next
            self.size += 1
        pred.next = new_node

    
    def remove_key(self, key):
        """
        Remmoves the node with the given key from the bucket.
        """
        prev = self.head
        curr = self.head.next 
        if curr is None:
            return
        while curr is not None:
            if curr.key == key:
                self.size -= 1
                prev.next = curr.next
                return
              
            prev = curr
            curr = curr.next
        return
    
    def search_val(self, key):
        """
        Finds the mapped value belonging to the key or returns -1 
        if key is not present.
        """
        curr = self.head        
        if curr.next is None:
            return -1
        while curr.next is not None:     
            curr = curr.next
            if curr.key == key:
                return curr.val           
        return -1