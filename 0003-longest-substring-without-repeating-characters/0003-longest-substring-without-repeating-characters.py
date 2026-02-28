class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        m = 0
        l = 0

        for r in s:
            while r in curr:
                curr.remove(s[l])
                l += 1
            curr.add(r)
            m = max(m, len(curr))

        return m