class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        val = 0

        while l <= r:
            m = (r + l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                val = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        l, r = 0, len(matrix[val]) - 1

        while l <= r:
            m = (r + l) // 2

            if matrix[val][m] == target:
                return True
            elif matrix[val][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False