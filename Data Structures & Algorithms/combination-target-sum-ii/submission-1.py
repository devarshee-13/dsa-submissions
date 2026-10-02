class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(pair, csum, start):

            if csum == 0:
                res.append(pair[:])
                return
            
            if csum < 0: return

            for i in range(start,len(candidates)):
                if i> start and candidates[i] == candidates[i-1]: continue

                csum -= candidates[i]
                pair.append(candidates[i])
                backtracking(pair,csum,i+1)
                csum += pair.pop()
        
        backtracking([],target,0)
        return res