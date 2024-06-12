# Time: O(n + p) where n = numCourses & p = prereqs
# Space: O(n + p) 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if preMap[course] == []:
                return True
            cycle.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            # set to empty arr bc we already know the prereqs are met
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
