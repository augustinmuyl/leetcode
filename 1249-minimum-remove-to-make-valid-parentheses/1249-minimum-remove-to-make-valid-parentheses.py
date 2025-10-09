class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openStack = []
        validString = []

        for i, v in enumerate(s):
            if v == "(" or v == ")":
                if v == "(":
                    openStack.append(len(validString))
                    validString.append(v)
                elif openStack:
                    openStack.pop()
                    validString.append(v)
            else:
                validString.append(v)
        
        for i in reversed(openStack):
            del validString[i]
        
        return "".join(validString)