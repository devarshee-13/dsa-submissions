class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashmap ={}
        for num in nums:
            hashmap[num] = 1

        def bt(per):
            if len(per) == len(nums):
                res.append(per[:])
                return
            
            for i in range(len(nums)):
                if hashmap[nums[i]] == 0:
                    continue
                per.append(nums[i])
                hashmap[nums[i]] = 0
                bt(per)
                hashmap[per.pop()]= 1

        bt([])
        return res