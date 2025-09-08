class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        A, S = [0] * len(temperatures), [[temperatures[0], 0]]

        for i, v in enumerate(temperatures[1:]):
            while v > S[-1][0]:
                A[S[-1][-1]] = i - S[-1][-1] + 1
                S.pop()
                if len(S) == 0:
                    break
            S.append([v, i+1])

        return A