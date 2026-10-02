# class Solution:
#     def rob(self, nums: List[int]) -> int:
       
class Solution:
    def rob(self, nums: List[int])-> int:
        n = len(nums)
        amt = 0 
        memo = {}
        def dfs(cur):
            if cur >= n:
                return 0
            if cur in memo:
                return memo[cur]
            take = nums[cur] + dfs(cur+2)
            skip = dfs(cur+1)
            memo[cur] = max(take,skip)
            return memo[cur]
    
        return dfs(0)