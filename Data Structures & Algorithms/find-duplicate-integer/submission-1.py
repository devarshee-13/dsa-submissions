class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for b in range(32):
            x=y=0
            mask = (1<<b)
            for num in nums:
                if num & mask:
                    x+= 1
            for i in range(1,len(nums)):
                if i & mask:
                    y+= 1
            
            if x>y:
                res = res|mask
        return res
        