class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def bt(indx,curSum,comb):
            if curSum == 0:
                res.append(comb[:])
                return
            
            for i in range(indx,len(nums)):
                curSum -= nums[i]
                if curSum<0: 
                    curSum+=nums[i]
                    return
                comb.append(nums[i])
                bt(i,curSum,comb)
                curSum+= comb.pop()
        
        bt(0,target,[])
        return res