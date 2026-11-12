class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for each in nums:
            if each in hashset:
                return True 
            hashset.add(each)
        return False