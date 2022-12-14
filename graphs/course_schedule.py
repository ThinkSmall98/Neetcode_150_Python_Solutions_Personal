# Time: O(n + p) where n = numCourses & p = prereqs, Space: O(n + p) 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            preMap[course] = [] # set to empty arr so we don't have to repeat work above
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
