class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for each in strs:
            key = ''.join(sorted(each))
            map[key].append(each)
        return list(map.values())