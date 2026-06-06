class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {} # map key to node
        self.left, self.right = Node(0,0), Node(0,0)
        # Left = LRU, right= most recent
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from l-list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    # insert node at right    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        self.hash[key] = Node(key, value)
        self.insert(self.hash[key])

        if len(self.hash) > self.capacity:
            # remove from the node from l-list and delete thr LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.hash[lru.key]

        
        
