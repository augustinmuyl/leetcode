class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        A = set()
        for i in nums[:k+1]:
            if i in A:
                return True
            A.add(i)
        
        for i in range(0, len(nums)-k-1, 1):
            A.remove(nums[i])
            if nums[i+k+1] in A:
                return True
            A.add(nums[k+i+1])
        return False
