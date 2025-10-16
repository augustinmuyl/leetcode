# for each cell run dfs on all neighboring cells
# stop if pacific or atlantic oceans -> successfull
# stop if val > original val -> unsuccessull

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = set()
        visited = set()

        def dfs(prev, r, c):
            pr, pc = prev
            if r < 0 or c < 0:
                return [True, False]
            if r >= rows or c >= cols:
                return [False, True]
            if heights[r][c] > heights[pr][pc] or (r, c) in visited:
                return [False, False]
            
            visited.add((r, c))

            flag = [False, False]
            for dr, dc in dirs:
                p, a = dfs((r, c), r + dr, c + dc)
                flag = [flag[0] or p, flag[1] or a]
            
            if flag == [True, True]:
                res.add((r, c))
            
            return flag
        
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                dfs((i, j), i, j)
                visited = set()
                
        return list(res)