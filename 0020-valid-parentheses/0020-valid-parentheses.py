class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        openList = {"(", "{", "["}
        openStack = []

        for i in s:
            if i in openList:
                openStack.append(i)
            elif openStack and bracketMap[i] == openStack[-1]:
                openStack.pop()
            else:
                return False
                    
        return False if openStack else True