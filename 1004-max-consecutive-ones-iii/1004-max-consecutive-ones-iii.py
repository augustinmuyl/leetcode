class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxnum, c, l = 0, 0, 0
        A = set()
        
        for i, v in enumerate(nums):
            if v == 0:
                c+=1
                A.add(i)
            if c > k:
                minA = min(A)
                l=minA+1
                A.remove(minA)
                c-=1
            maxnum = max(maxnum, i+1 - l)
        return maxnum
