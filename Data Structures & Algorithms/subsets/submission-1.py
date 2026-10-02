class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []  
        subset = []      

        def backtrack(indx):
            if indx <= len(nums):
                res.append(subset[:])

            if indx > len(nums):
                return
            
            for i in range(indx,len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
       
        backtrack(0)
        return res