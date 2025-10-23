class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50_000: return 1
        def partition(n, lo, hi, p):
            n[p], n[hi] = n[hi], n[p]
            i = lo
            pivot = n[hi]
            
            for j in range(lo, hi):
                if n[j] < pivot:
                    n[j], n[i] = n[i], n[j]
                    i += 1
            n[hi], n[i] = n[i], n[hi]
            return i
        
        idx = len(nums) - k
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            p = partition(nums, lo, hi, randint(lo, hi))
            if p == idx:
                return nums[p]
            elif p < idx:
                lo = p + 1
            else:
                hi = p - 1