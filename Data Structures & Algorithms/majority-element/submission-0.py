class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for each in nums:
            map[each] += 1
        for key,val in map.items():
            if val >= (len(nums)/2):
                return key