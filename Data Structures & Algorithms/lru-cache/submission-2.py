class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = []
    
    def put(self, key:int, value:int):
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)
                return
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key,value])
        return
    
    def get(self, key:int)->int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1