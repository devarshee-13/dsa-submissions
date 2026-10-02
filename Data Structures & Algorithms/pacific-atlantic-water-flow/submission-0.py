class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:    
        pacific = set()
        atlantic = set()
        nrows, ncols = len(heights), len(heights[0])
        res=[]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()

        def dfs(r,c, visited, prevHeight):
            if ((r,c) in visited or 
                r<0 or c<0 or
                r == nrows or c ==ncols or
                heights[r][c] < prevHeight): 
                return
            visited.add((r,c))
            
            for dr,dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])

        
        for c in range(ncols):
            dfs(0,c,pacific,heights[0][c])
            dfs(nrows-1,c,atlantic,heights[nrows-1][c])
        
        for r in range(nrows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,ncols-1,atlantic,heights[r][ncols-1])

        for r in range(nrows):
            for c in range(ncols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res           