class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]
       
        def backtrack(row):
            if row == n:
                boardcopy = ["".join(eachrow) for eachrow in board]      # VVV IMP
                res.append(boardcopy)
                return  
            
            for col in range(n):
                if col in columns or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                
                board[row][col] = "Q"
                # columns.append(col)             #set doesnt have .append(). use add()
                columns.add(col)           
                posDiag.add(row+col)
                negDiag.add(row-col)

                backtrack(row + 1)

                board[row][col] = "."
                columns.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)

        backtrack(0)
        return res