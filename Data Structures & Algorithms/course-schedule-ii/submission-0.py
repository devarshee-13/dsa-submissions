class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        stack = []
        
        for crs,pre in prerequisites:
            depMap[crs].append(pre)
            indegree[pre] += 1
        print(depMap)
        q =deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        while q:
            course = q.popleft()
            stack.append(course)
            for nei in depMap[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(len(stack))
        print(stack[::-1])
        if len(stack) == numCourses:
            return stack[::-1]
        else: return []
