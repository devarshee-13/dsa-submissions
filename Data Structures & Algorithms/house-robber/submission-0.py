class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0]* (len(nums)+1)

        def dfs(i):
            if i >= len(nums): return 0
            if cache[i]: return cache[i]
            
            cache[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            
            return cache[i]
        
        return dfs(0)