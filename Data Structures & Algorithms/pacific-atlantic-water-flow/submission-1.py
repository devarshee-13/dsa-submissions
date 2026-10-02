class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        nrows = len(heights)
        ncols = len(heights[0])
        directions =  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac_res = [[False]*ncols for i in range(nrows)]
        atl_res = [[False]*ncols for i in range(nrows)]

        pacific = [] 
        atlantic = []

        for c in range(ncols):
            pacific.append((0,c))
            atlantic.append((nrows-1,c))
        for r in range(nrows):
            pacific.append((r,0))
            atlantic.append((r,ncols-1))
        
        def bfs(source,ocean):
            q = deque(source)
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (0<=nr<nrows and 0<=nc<ncols and 
                        not ocean[nr][nc] and 
                        heights[nr][nc]>= heights[r][c]):
                        q.append((nr,nc))
        
        bfs(pacific,pac_res)
        bfs(atlantic,atl_res)

        res = []
        for r in range(nrows):
            for c in range(ncols):
                if pac_res[r][c] and atl_res[r][c]:
                    res.append([r,c])
        return res