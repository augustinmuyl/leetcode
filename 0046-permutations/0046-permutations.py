class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = deque(nums)

        def dfs(curr, subset):
            if not curr:
                res.append(subset.copy())
                return

            for i in range(len(curr)):
                subset.append(curr.pop())
                dfs(curr, subset)
                curr.appendleft(subset.pop())

        dfs(curr, [])
        return res