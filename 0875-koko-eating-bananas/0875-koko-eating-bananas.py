class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        
        def traverse(k: int) -> int:
            c = 0
            for i in piles:
                if i == k:
                    c += 1
                else:
                    c += (i // k) + 1
            return c

        while True:
            mid = (lo + hi) // 2
            
            if traverse(lo) <= h:
                return lo
            elif traverse(mid) <= h:
                hi = mid
            else:
                lo = mid + 1