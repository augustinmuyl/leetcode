class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum() or not s[r].isalnum():
                if not s[l].isalnum():
                    l+=1
                else:
                    r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
