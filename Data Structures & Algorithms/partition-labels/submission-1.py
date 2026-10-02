class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        res = []
        end = size = 0
        for indx,c in enumerate(s):
            lastIndex[c] = indx
        
        for indx,c in enumerate(s):
            size += 1
            end = max(end,lastIndex[c])
            if indx == end:
                res.append(size)
                size = 0
        return res