class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, curr_area = 0, 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            nonlocal curr_area
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
                return

            curr_area += 1
            grid[r][c] = 0

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, curr_area)
                    curr_area = 0

        return max_area