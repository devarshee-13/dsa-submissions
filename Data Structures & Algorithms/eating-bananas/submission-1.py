class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        
        piles.sort()
        l,r= 1, piles[-1]
        res = r
        
        while l <= r:
            m = (l+r)//2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p)/m)
            if hours<=h:
                res = m
                r= m-1
            else:
                l = m+1
        
        return res