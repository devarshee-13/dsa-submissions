class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        res = nums[0]

        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m

        pivot = l

        def bs(l,r):
            while l<=r:
                m = (l+r)//2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            return -1
        
        res1 = bs(0,pivot-1)
        res2 = bs(pivot,len(nums)-1)

        if res1!= -1: return res1
        return res2