class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        minCost = 0
        mem = {}
        mem[0] = cost[0]
        mem[1] = cost[1]
        n = len(cost)
        def dfs(cur):
            if cur in mem: return mem[cur]
            mem[cur] = cost[cur] + min(dfs(cur-1),dfs(cur-2))
            return mem[cur]
        return min(dfs(n-1),dfs(n-2))