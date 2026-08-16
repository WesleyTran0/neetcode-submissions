class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Map each course to its prereq
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # courses that a SINGLE dfs call has seen
        seen = set()

        def dfs(crs):
            # a cycle is detected
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
        
            seen.add(crs)
            for pre in preMap[crs]:
                # if one of the pre reqs also reach a cycle, return False (since they reached a cycle)
                if not dfs(pre):
                    return False

            seen.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            