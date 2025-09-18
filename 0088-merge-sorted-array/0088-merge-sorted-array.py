class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        A, B = nums1, nums2
        a, b, c = len(A) - 1, len(B) - 1, 0

        while a >= 0:
            if A[a] == 0 and c < n:
                A[a], B[b] = B[b], A[a]
                b -= 1
            else:
                i = a
                while i + 1 < len(A) and A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    i += 1
            a -= 1
            c += 1