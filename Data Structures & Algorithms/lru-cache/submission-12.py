from typing import Tuple

class Node:
    def __init__(self, kv: Tuple[int, int]= (0, 0), next = None, prev = None):
        self.key, self.val = kv
        self.next = next
        self.prev = prev


class LRUCache:
    '''
    Left <-> LRU <-> ... <-> MRU <-> Right
    '''

    def __init__(self, capacity: int):
        self.left, self.right = Node(), Node()

        self.cap = capacity

        # key -> node
        self.values = {}

        self.left.next = self.right
        self.right.prev = self.left
    

    def insert(self, node):
        prev = self.right.prev
        
        node.prev = prev
        prev.next = node

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev        

      
    def get(self, key: int) -> int:       
        if key in self.values:
            node = self.values[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.remove(self.values[key])
        
        node = Node((key, value))
        self.values[key] = node
        self.insert(node)

        if len(self.values) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.values[LRU.key]




        


        

      