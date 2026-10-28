class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> res = {intervals[0]};

        for (const auto& interval : intervals) {
            int& curr = res.back()[1];
            
            if (curr < interval[0]) res.push_back(interval);
            else curr = max(curr, interval[1]);
        }

        return res;
    }
};