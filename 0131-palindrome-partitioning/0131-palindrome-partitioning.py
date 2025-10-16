class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(str):
            l, r = 0, len(str) - 1

            while l < r:
                if str[l] != str[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        def dfs(subset, skipped, i):
            if i >= len(s):
                print(subset)
                if isPalindrome(subset):
                    res.append([subset, [i for i in s]])
                return
            
            subset += s[i]
            dfs(subset, skipped, i + 1)
            subset = subset[:len(subset) - 1]
            while i + 1 < len(s) and s[i + 1] == s[i]:
                i += 1
            skipped = s[i]
            dfs(subset, skipped, i + 1)
        
        dfs("", "", 0)
        return res