class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        key = len(nums)//2
        return nums[key]