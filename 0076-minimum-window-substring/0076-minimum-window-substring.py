class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checkKeys(A: dict, B: dict) -> bool:
            if B.keys() != A.keys():
                return False
            for i in B.keys():
                if B[i] < A[i]:
                    return False
            return True

        A, B = {}, {}
        l, res = 0, ""

        for i in t:
            A[i] = A.get(i, 0) + 1

        for r in range(len(s)):
            if s[r] in A:
                B[s[r]] = B.get(s[r], 0) + 1

            while checkKeys(A, B):
                B[s[l]] = B.get(s[l], 0) - 1
                if B[s[l]] <= 0:
                    B.pop(s[l])
                if r - l + 1 < len(res) or res == "":
                    res = s[l : r + 1]
                l += 1

        return res