class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = newInterval

        for i, v in enumerate(intervals):
            if v[0] > curr[1]:
                res.append(curr)
                return res + intervals[i:]
            if v[1] < curr[0] or not curr:
                res.append(v)
            else:
                if v[1] >= curr[0] and v[0] <= curr[1]:
                    curr = [min(v[0], curr[0]), max(v[1], curr[1])]
            
        res.append(curr)
        
        return res