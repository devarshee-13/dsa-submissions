# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         Map = {}
#         for indx,val in enumerate(nums):
#             Map[val] = indx
        
#         for val,indx in Map.items():
#             diff = target-val
#             if diff in Map and Map[diff] != indx:
#                 return [indx,Map[target-val]]
#         return []

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List:

        hashmap = {}
        for indx, val in enumerate(nums):
            hashmap[val] = indx

        for indx,val in enumerate(nums):
            if (target-val) in hashmap and hashmap[target-val] != indx:
                return [indx,hashmap[target-val]]