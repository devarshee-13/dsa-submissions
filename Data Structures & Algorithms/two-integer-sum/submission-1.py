# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map = {}
        # for indx,val in enumerate(nums):
        #     Map[val] = indx
        
        # for val,indx in Map.items():
        #     if (target-val) in Map:
        #         return [indx,Map[target-val]]
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List:

        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1,len(nums)):
                if diff == nums[j]:
                    return [i,j]