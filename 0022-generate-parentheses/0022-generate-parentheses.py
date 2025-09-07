class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        A = []
        return(self.generateParenthesisRec("", n, 0, 0, A))
    
    def generateParenthesisRec(self, s: str, n: int, opened: int, closed: int, A: list) -> str:
        if opened == closed == n:
            A.append(s)
        
        if opened <= n:
            if closed < opened:
                self.generateParenthesisRec(s + "(", n, opened + 1, closed, A)
                self.generateParenthesisRec(s + ")", n, opened, closed + 1, A)
            else:
                self.generateParenthesisRec(s + "(", n, opened + 1, closed, A)
        
        return A