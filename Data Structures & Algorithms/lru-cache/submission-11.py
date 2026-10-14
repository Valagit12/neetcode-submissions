class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None
    
    def __str__(self):
        return f"({self.key}:{self.val} - before {self.prev.val} - after {self.next.val})"


class LRUCache:
    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.keys = {}
        self.left, self.right = Node(0, 0), Node(0, 0) #right is most recent, left is least recent
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        MRU = self.right.prev
        # left -> LRU -> .. -> MRU-> right
        node.prev = MRU
        # left -> LRU -> .. -> MRU <- node right
        node.next = self.right
        # left <-> LRU <-> .. -> MRU <- node -> right
        MRU.next = node
        # left <-> LRU <-> .. -> MRU <-> node -> right
        self.right.prev = node
        # left <-> LRU <-> .. -> MRU <- node <-> right

    def remove(self, node):
        nextnode = node.next
        prevnode = node.prev

        nextnode.prev = prevnode
        prevnode.next = nextnode      


    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1
       

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.remove(self.keys[key])
        node = Node(key, value)
        self.insert(node)
        self.keys[key] = node

        if len(self.keys) > self.cap:
            LRU = self.left.next
            print('LRU: ', LRU)
            self.remove(LRU)
            del self.keys[LRU.key]

        
