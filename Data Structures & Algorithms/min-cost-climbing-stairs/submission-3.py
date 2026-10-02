class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        n = len(cost)
        prev1 = cost[0]
        prev2 = cost[1]
        for cur in range(2,n):    
            curCost = cost[cur] + min(prev1,prev2)
            prev1 = prev2
            prev2 = curCost
        
        return min(prev1,prev2)