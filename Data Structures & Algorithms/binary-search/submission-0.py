class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(l,r):
            if l>r:
                return -1
            m = (l+r)//2     
            if nums[m] == target:
                return m
            if target > nums[m]:
                return bs(m+1,r)
            else:
                return bs(l,m-1)
        
        return bs(0,len(nums)-1)