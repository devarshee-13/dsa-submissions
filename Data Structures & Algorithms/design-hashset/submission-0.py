# class MyHashSet:

#     def __init__(self):
        

#     def add(self, key: int) -> None:
        

#     def remove(self, key: int) -> None:
        

#     def contains(self, key: int) -> bool:
        


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)

class ListNode:
    def __init__(self, node_key:int):
        self.node_key = node_key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]    # 10^4 because see the constraints.
        # self.set = ListNode(0) * 10**4     this is wrong, this will give one single Array of 10^4 list nodes, not 10^4 separate list nodes. we want individual nodes

    def add(self, key:int)->None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.node_key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key:int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.node_key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
    def contains(self, key:int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.node_key == key:
                return True
            cur = cur.next
        return False