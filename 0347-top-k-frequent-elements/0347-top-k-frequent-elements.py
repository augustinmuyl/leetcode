class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = {}
        B = [[] for _ in range(len(nums) + 1)]
        C = []
        for i in nums:
            A.update({i: A.get(i, 0) + 1})
        for i in A:
            B[A.get(i)].append(i)
        for i in range(len(B) - 1, 0, -1):
            if B[i]:
                if (len(C) >= k):
                    break
                for j in B[i]:
                    C.append(j)
        return C
        