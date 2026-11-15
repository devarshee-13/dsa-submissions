class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        Map = {}

        for indx, val in enumerate(nums):
            diff = target - val
            if diff in Map and Map[diff] != indx:
                return [Map[diff],indx]
            Map[val] = indx
