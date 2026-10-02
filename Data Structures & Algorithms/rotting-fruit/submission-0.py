class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        time = 0
        fresh = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col]==1:
                    fresh+= 1
        
        while q and fresh>0:
            time+= 1
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    
                    if (r+dr < 0 or c+ dc < 0 or
                        r+dr>=ROWS or c+dc >= COLS or
                        grid[r+dr][c+dc] != 1): continue

                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    q.append((r+dr,c+dc))
        
        if fresh == 0:
            return time
        else: return -1        