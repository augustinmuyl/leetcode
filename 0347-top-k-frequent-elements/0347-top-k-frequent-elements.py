class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = {}
        B = [[] for i in range(len(nums) + 1)]
        C = []
        
        for i in nums:
            if i not in A:
                A.update({i:1})
            else:
                A.update({i:A.get(i)+1})
        
        for key, val in A.items():
            B[val].append(key)

        for i in range(len(B)-1, 0, -1):
            for j in B[i]:
                if len(C) < k:
                    C.append(j)
        
        return C
        