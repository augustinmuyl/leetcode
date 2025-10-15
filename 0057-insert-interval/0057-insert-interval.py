class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, v in enumerate(intervals):
            if v[1] < newInterval[0]:
                res.append(v)
            elif v[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(v[0], newInterval[0]), max(v[1], newInterval[1])]
        
        res.append(newInterval)
        
        return res