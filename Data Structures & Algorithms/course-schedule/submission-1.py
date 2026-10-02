class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = defaultdict(list)
        for crs, pre in prerequisites:
            depMap[crs].append(pre)       
        visiting = set()

        def dfs(course):
            if course in visiting: return False
            if depMap[course] == []: return True

            visiting.add(course)
            for nei in depMap[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            depMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True