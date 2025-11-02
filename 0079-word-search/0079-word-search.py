class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True
            elif r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))

            res = False
            for dr, dc in dirs:
                res = res or dfs(r + dr, c + dc, i + 1)
            visited.remove((r, c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False