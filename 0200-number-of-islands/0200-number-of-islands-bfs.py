class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                cr, cc = q.popleft()
                if cr == len(grid)  or cc == len(grid[cr]) or grid[cr][cc] == "0":
                    continue
                grid[cr][cc] = "0"
                
                q.append((cr, cc + 1))
                if cc != 0: q.append((cr, cc - 1))
                q.append((cr + 1, cc))
                if cr != 0: q.append((cr - 1, cc))

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)

        return res