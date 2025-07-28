class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        A = {}
        l, m, mfreq = 0, 0, 0

        for r in range(len(s)):
            A[s[r]] = A.get(s[r], 0) + 1
            mfreq = max(mfreq, A[s[r]])

            while r - l + 1 - mfreq > k:
                A[s[l]] -= 1
                l += 1

            m = max(m, r - l + 1)

        return m