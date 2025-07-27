class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        A = []
        O = {"+", "-", "*", "/"}

        for i in tokens:
            if i not in O:
                A.append(i)
            else:
                prev = int(A.pop())
                if i == "+":
                    A.append(int(A.pop()) + prev)
                elif i == "-":
                    A.append(int(A.pop()) - prev)
                elif i == "*":
                    A.append(int(A.pop()) * prev)
                else:
                    A.append(int(A.pop()) / prev)

        return A[0]