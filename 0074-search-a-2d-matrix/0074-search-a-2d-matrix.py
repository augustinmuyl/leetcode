class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(matrix, target):
            top, bottom = 0, len(matrix) - 1

            while top <= bottom:
                mid = (top + bottom) // 2

                if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid + 1][0] <= target:
                    top = mid + 1
                else:
                    bottom = mid - 1
        
        row = findRow(matrix, target)
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if mid == target:
                return True
            elif target < mid:
                r = mid - 1
            else:
                l = mid + 1
        
        return False