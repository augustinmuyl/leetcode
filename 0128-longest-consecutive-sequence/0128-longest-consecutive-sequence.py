class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        c, m = 1, 1

        for i in S:
            if i - 1 not in S:
                c = 1
                n = i
                while n + 1 in S:
                    c += 1
                    n += 1
                m = max(m, c)
        
        return 0 if not nums else m