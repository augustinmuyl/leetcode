class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = list(sorted(nums1 + nums2))
        mid = nums[len(nums)//2]
        if len(nums)%2 == 1:
            return mid
        else:
            return (mid + nums[len(nums)//2 - 1]) / 2
