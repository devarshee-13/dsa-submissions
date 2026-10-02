class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {n:1}
        def dfs(cur):
            if cur in mem:
                return mem[cur]
            if cur > n:
                return 0
            if cur < n:
                mem[cur] = dfs(cur+1) + dfs(cur+2)
                return mem[cur]
        
        return dfs(0)