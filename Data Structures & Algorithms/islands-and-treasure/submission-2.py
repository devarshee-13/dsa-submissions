class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        nrows =len(grid)
        ncols = len(grid[0])
        q = deque()
        visit = set()
        distance =0
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
   
        while q:
            distance += 1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    if (r+dr<0 or c+dc<0 or
                    r+dr >=nrows or c+dc>= ncols or
                    grid[r+dr][c+dc] != 2147483647 or 
                    (r+dr,c+dc)in visit): continue

                    grid[r+dr][c+dc] = distance
                    q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))