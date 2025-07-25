class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A, B = {}, {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            A[s[i]] = A.get(s[i], 0) + 1
            B[t[i]] = B.get(t[i], 0) + 1
        for i in A:
            if A.get(i) != B.get(i):
                return False
        
        return True