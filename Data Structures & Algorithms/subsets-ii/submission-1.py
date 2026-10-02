class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(start,subset):
            if start > len(nums):
                return
            
            res.append(subset[:])
            
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue                
                subset.append(nums[i])
                bt(i+1, subset)
                subset.pop()
        
        bt(0,[])
        return res