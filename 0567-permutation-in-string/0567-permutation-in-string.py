class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A, B = {}, {}
        l = 0

        for i in s1:
            A[i] = A.get(i, 0) + 1

        for r in range(len(s2)):
            B[s2[r]] = B.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                B[s2[l]] = B.get(s2[l], 0) - 1
                if B[s2[l]] == 0:
                    B.pop(s2[l])
                l += 1

            if A == B:
                return True

        return False