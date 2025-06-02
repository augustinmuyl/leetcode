class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        A = {}

        for i, l in enumerate(board):
            for j, n in enumerate(l):
                if n != ".":
                    if n not in A:
                        A.update({n: [[j, i]]})
                    else:
                        A.get(n).append([j, i])
        
        for i in A:
            X = set()
            Y = set()
            for j in A.get(i):
                X.add(j[0])
                Y.add(j[1])
                for k in A.get(i):
                    if not (j[0] == k[0] and j[1] == k[1]):
                        if (j[0] // 3 == k[0] // 3) and (j[1] // 3 == k[1] // 3):
                            return False
            if len(X) != len(A.get(i)) or len(Y) != len(A.get(i)):
                return False            
        
        return True    
        