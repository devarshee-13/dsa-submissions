class Solution:
    def rob(self, nums: List[int]) -> int:
        # state: dp[i] = max amount up to house i
        n=len(nums)
        if n == 1: return nums[0]
        
        def dfs(start,end):

            if start > end:
                return 0
            dp = [0]*(n+2)

            for i in range(end,start -1,-1):
                dp[i] = max(dp[i+1],dp[i+2]+nums[i])
            
            return dp[start]       

        return max(dfs(0,n-2),dfs(1,n-1))