class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
       prev = node.prev
       nxt = node.next
       prev.next = nxt
       nxt.prev = prev

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.next = nxt
        node.prev = prev
        nxt.prev = node

    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache.pop(key)

        if len(self.cache) >= self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

    def get(self,key):
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].value