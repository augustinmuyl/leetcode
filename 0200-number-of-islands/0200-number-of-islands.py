class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[r]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r, c + 1)
            if c != 0: dfs(r, c - 1)
            dfs(r + 1, c)
            if r != 0: dfs(r - 1, c)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res