class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        A = []
    
        def backtrack(s: str, opened: int, closed: int) -> str:
            if opened == closed == n:
                A.append(s)
            
            if opened <= n:
                backtrack(s + "(", opened + 1, closed)
            if closed < opened:
                backtrack(s + ")", opened, closed + 1)
            
            return A
        
        return(backtrack("", 0, 0))