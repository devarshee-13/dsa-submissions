class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []

        def backtracking(pair, cSum,i):
            if cSum == 0:
                res.append(pair[:])
                return
            if cSum <0: return
            
            if i < len(nums):
                cSum = cSum - nums[i]
                print(cSum)
                pair.append(nums[i])
                backtracking(pair,cSum,i)
                pair.pop()
                cSum = cSum+nums[i]
            if i+1 < len(nums): backtracking(pair,cSum,i+1)

        backtracking([],target,0)

        return res