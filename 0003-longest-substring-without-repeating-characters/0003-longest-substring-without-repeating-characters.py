class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxval = 0
        S = {}

        for i in range(len(s)):
            if s[i] in S:
                l = max(l, S[s[i]] + 1)
            S.update({s[i]: i})
            maxval = max(maxval, i+1 - l)
        
        return maxval
        