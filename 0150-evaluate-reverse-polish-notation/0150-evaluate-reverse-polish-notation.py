class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            elif i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                tmp = int(stack.pop())
                stack.append(int(stack.pop()) / tmp)
            elif i == "-":
                tmp = int(stack.pop())
                stack.append(int(stack.pop()) - tmp)
        
        return int(stack[0])