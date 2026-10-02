class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        visit = set()
        nrows,ncols = len(grid), len(grid[0])
        land = 0
        q = deque()
        def bfs(row,col):
            nonlocal q
            q.append((row,col))
            visit.add((row,col))
            
            while q:
                r,c = q.popleft()
                visit.add((r,c))
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<nrows and 0<=nc<ncols and grid[nr][nc] == '1' and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
        
        for r in range(nrows):
            for c in range(ncols):
                if (r,c) not in visit and grid[r][c] == '1':
                    bfs(r,c)
                    land += 1
        return land