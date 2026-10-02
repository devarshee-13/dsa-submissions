# class Solution:
    # same as house robber 1
    # extra: 
    #    Rob from house 0 to n-2 (exclude last house)
    #    Rob from house 1 to n-1 (exclude first house)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        def dfs(curr,last):
            if (curr,last) in memo:
                return memo[(curr,last)]
            if curr > last:
                return 0
            take_curr = nums[curr] + dfs(curr+2, last)
            skip_curr = dfs(curr+1,last)
            memo[(curr,last)] = max(take_curr,skip_curr)
            return memo[(curr,last)]

        return max(dfs(0,n-2),dfs(1,n-1))
       