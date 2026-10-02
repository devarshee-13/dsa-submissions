class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(curStep):
            if curStep == n: return 1       # 1 path found
            if curStep > n:  return 0       # 0 path found

            if cache[curStep] != -1: 
                return cache[curStep]        
            
            cache[curStep] = dfs(curStep+1) + dfs(curStep+2)
            
            return cache[curStep]
        
        return dfs(0)
    
    # this forms a binary recursive tree but with memory stored
    # TC = O(n)
    # SC = O(n)