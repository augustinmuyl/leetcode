class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parens = []
        invalid = set()

        for i, v in enumerate(s):
            if v == "(":
                open_parens.append(i)
            elif v == ")":
                if open_parens:
                    open_parens.pop()
                else:
                    invalid.add(i)
        
        invalid.update(open_parens)
        
        return "".join([s[i] for i in range(len(s)) if i not in invalid])