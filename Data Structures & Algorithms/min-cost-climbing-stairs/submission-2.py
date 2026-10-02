class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        n = len(cost)
        dp=[0]*(n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for cur in range(2,n):    
            dp[cur] = cost[cur] + min(dp[cur-1],dp[cur-2])
            print(dp)
        
        return min(dp[n-2],dp[n-1])