import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ed =[]
        res = []
        for indx, point in enumerate(points):
            x,y = point[0],point[1]
            ed.append((math.sqrt(x**2 + y**2),indx))

        heapq.heapify(ed) 
        print(ed)
        for i in range(k): 
            dst,indx = heapq.heappop(ed)
            res.append(points[indx])
        
        return res