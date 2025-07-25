class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(list(set(nums)))
        c, m = 1, 1

        for r in range(len(n) - 1):
            if n[r] + 1 == n[r + 1]:
                c += 1
            else:
                c = 1
            m = max(m, c)
        
        return 0 if nums == [] else m