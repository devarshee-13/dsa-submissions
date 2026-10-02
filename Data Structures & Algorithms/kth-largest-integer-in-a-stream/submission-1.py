import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):    # O(n log n)
        self.k = k
        self.minH = nums
        heapq.heapify(self.minH)         #  O(n) 
        while len(self.minH) > self.k:   
            heapq.heappop(self.minH)     #  O(log n) * n
    
    def add(self, val: int) -> int:         # O(n log n)
        heapq.heappush(self.minH,val)    # O(log n)
        while len(self.minH) > self.k: 
            heapq.heappop(self.minH)       # O(log n) * n
        
        return self.minH[0]     # O(1)