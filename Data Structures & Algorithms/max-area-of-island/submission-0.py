class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_area = 0
        visit = set()

        def bfs(row,col):
            local_area = 0
            q = deque()
            q.append((row,col))
            visit.add((row,col))
            while q:
                r,c = q.popleft()
                local_area += 1
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (0<=nr<nrows and 0<=nc<ncols) and ((nr,nc) not in visit) and grid[nr][nc] ==1:
                        visit.add((nr,nc))
                        q.append((nr,nc))
            return local_area
        
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    local_area = bfs(r,c)
                    max_area = max(max_area,local_area)
        
        return max_area