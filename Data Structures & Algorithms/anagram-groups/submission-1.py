from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for each in strs:
            count = [0] * 26

            for s in each:
                count[ord(s) - ord('a')] += 1
            
            map[tuple(count)].append(each)
        
        return list(map.values())