class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for _ in range(numCourses)]
        visited = set()

        for i in prerequisites:
            preMap[i[0]].append(i[1])
        
        def dfs(i):
            if i in visited:
                return False
            if preMap[i] == []:
                return True
            
            visited.add(i)

            for j in range(len(preMap[i])):
                if not dfs(preMap[i][j]):
                    return False

            visited.remove(i)
            preMap[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True