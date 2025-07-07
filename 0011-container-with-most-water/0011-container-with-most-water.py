class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, amax = 0, len(height) - 1, 0
        while l < r:
            a = (r - l) * min(height[l], height[r])
            amax = max(a, amax)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return amax
