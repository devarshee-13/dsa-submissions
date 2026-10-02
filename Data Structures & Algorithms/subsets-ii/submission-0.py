class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(subset,start):
            if start> len(nums):
                return
            else:                
                res.append(subset[:])

            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtracking(subset,i+1)
                subset.pop()
            
        backtracking([],0)
        return res
        