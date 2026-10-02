class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = defaultdict(list)
        visit = set()
        indegree = [0]*numCourses
        order = []
        for before,after in prerequisites:
            depMap[before].append(after)
            indegree[after] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            order.append(course)
            for dep in depMap[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
        
        return len(order) == numCourses