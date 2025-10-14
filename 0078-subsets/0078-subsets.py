#     yes/no
#    yes / no   |   yes  /   no
#yes/no | yes/no | yes/no | yes/no

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, i):
            if i == len(nums):
                res.append(curr)
                return curr
            
            dfs(curr + [nums[i]], i + 1)
            dfs(curr, i + 1)
        
        dfs([], 0)
        return res