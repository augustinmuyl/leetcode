class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()

        def dfs(prev, ocean, r, c):
            pr, pc = prev
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < heights[pr][pc] or (r, c) in ocean:
                return
            
            ocean.add((r, c))
            for dr, dc in dirs:
                dfs((r, c), ocean, r + dr, c + dc)
        
        for i in range(cols):
            dfs((0, i), pac, 0, i)
            dfs((rows - 1, i), atl, rows - 1, i)
        
        for i in range(rows):
            dfs((i, 0), pac, i, 0)
            dfs((i, cols - 1), atl, i, cols - 1)
                
        return list(pac & atl)