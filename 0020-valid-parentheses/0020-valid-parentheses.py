class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = {'(', '{', '['}
        CLOSED = {')': '(', '}': '{', ']': '['}
        A = []

        for i in s:
            if i in CLOSED:
                if CLOSED[i] == A[-1]:
                    A.pop()
                else:
                    return False
            if i in OPEN:
                A.append(i)
        
        return True if not A else False