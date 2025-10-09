class Solution:
    def decodeString(self, s: str) -> str:
        def decodeStringRec(s: str, num: int) -> str:
            stack = []
            dq = deque([])
            digit = deque([])
            res = ""

            for i, v in enumerate(s):
                if v == "]":
                    while not stack[-1].isdigit():
                        if stack[-1] != "[":
                            dq.appendleft(stack[-1])
                        stack.pop()
                    
                    while stack and stack[-1].isdigit():
                        digit.appendleft(stack.pop())
                    stack.append(int("".join(digit)) * ("".join(dq)))
                    dq.clear()
                    digit.clear()
                else:
                    stack.append(v)
            
            return "".join(stack)
        
        return decodeStringRec(s, 1)