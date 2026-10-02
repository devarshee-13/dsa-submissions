class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] = 1
        
        def backtracking(pair):
            if len(pair) == len(nums):
                res.append(pair[:])
                return
            
            for i in range(len(nums)):
                if hashmap[nums[i]] == 0:
                    continue
                
                pair.append(nums[i])
                hashmap[nums[i]] = 0
                backtracking(pair)
                num = pair.pop()
                hashmap[num] = 1
        backtracking([])

        return res