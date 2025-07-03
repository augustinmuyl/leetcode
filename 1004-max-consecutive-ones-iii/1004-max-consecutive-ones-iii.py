class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxnum, c, l = 0, 0, 0
        A = deque([])
        
        for i, v in enumerate(nums):
            if v == 0:
                c+=1
                A.append(i)
            if c > k:
                l=A.popleft()+1
                c-=1
            maxnum = max(maxnum, i+1 - l)
        return maxnum
