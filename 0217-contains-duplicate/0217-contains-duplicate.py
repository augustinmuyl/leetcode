class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        A = set()

        for i in nums:
            if i in A:
                return True
            A.add(i)
        
        return False