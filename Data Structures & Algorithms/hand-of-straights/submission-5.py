class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = {}
        for n in hand: 
            count[n] = 1+count.get(n,0)
        
        minH = list(count.keys())
        heapq.heapify(minH)  

        while minH:
            i = minH[0]
            for x in range(i, i + groupSize):
                if x not in count: return False
                count[x] -= 1
                if count[x] == 0: 
                    if x!= minH[0]:
                        return False
                    heapq.heappop(minH)

        return True