class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i:[] for i in range(numCourses)}
        visiting = set()
        visited = set()
        stack = []
        
        for crs,pre in prerequisites:
            depMap[crs].append(pre)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for nei in depMap[course]:
                if not dfs(nei): return False
            visiting.remove(course)
            visited.add(course)
            stack.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return stack