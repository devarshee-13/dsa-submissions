import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]           # SC =O(n)
        heapq.heapify(stones)           # O(n)

        while len(stones) > 1:              # O(n)
            y = -heapq.heappop(stones)      # O(log n)
            x = -heapq.heappop(stones)      # O(log n)
            if x == y:
                continue
            elif x<y: heapq.heappush(stones, -(y-x))        # O(log n)

        if stones: 
            return -stones[0]        # O(1)
        else: return 0

# TC = O(n log n)
# SC = O(n)