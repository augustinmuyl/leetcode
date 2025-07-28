class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = []

        for i in matrix:
            M += i

        l, r = 0, len(M) - 1

        for i in M:
            m = (r + l) // 2

            if M[m] == target:
                return True
            elif M[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False