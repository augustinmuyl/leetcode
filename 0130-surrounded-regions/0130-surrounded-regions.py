class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return True
            elif board[r][c] == "X" or (r, c) in visited:
                return False

            visited.add((r, c))
            flag = False
            for dr, dc in dirs:
                flag = flag or dfs(r + dr, c + dc)
            
            return flag
        
        def rep_dfs(r, c):
            if board[r][c] == "X":
                return
            
            board[r][c] = "X"
            for dr, dc in dirs:
                rep_dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    flag = dfs(r, c)
                    visited = set()
                    if not flag:
                        rep_dfs(r, c)