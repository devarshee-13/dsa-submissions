class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        res = False

        def dfs(r,c,indx):
            nonlocal res
            if indx == len(word):
                return True
            
            if (r<0 or c<0 or r>= nrows or c >=ncols or
                board[r][c] != word[indx] or
                board[r][c] == "#" ):
                return False
            
            board[r][c] = "#"
            for dr,dc in directions:
                if dfs(r+dr,c+dc,indx+1):
                    res = True
            
            board[r][c] = word[indx]
            return res
        
        for r in range(nrows):
            for c in range(ncols):
                if dfs(r,c,0): return True
        return False