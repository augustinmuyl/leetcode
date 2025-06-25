class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxval = 0
        S = {""}

        for i in range(len(s)):
            if s[i] not in S:
                S.add(s[i])
            else:
                if s[l] == s[i]:
                    l+=1
                else:
                    while (s[l] != s[i]):
                        S.remove(s[l])
                        l+=1
                    l+=1
            maxval = max(maxval, i+1 - l)
            print(l, i, S)
        
        return maxval
        