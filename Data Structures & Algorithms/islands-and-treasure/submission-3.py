class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        nrows =len(grid)
        ncols = len(grid[0])
        q = deque()
        dist = 0

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            dist += 1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<nrows and 0<=nc<ncols and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist
                        q.append((nr,nc))