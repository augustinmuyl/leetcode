class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digit = deque([])

        for i, v in enumerate(s):
            if v != "]":
                stack.append(v)
            else:
                substr = ""
                digit = ""

                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit) * substr)
        
        return "".join(stack)