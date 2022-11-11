# Time: O(E + V), E = edges & V = vertices, Space: O(E + V)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False
            visited.add(course)
            cycle.remove(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
