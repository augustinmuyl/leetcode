class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        int i = -1;

        sort(intervals.begin(), intervals.end());

        for (const auto& interval : intervals) {
            if (res.empty() || res[i][1] < interval[0]) {
                res.push_back(interval);
                i++;
            } else {
                res[i][1] = max(res[i][1], interval[1]);
            }
        }

        return res;
    }
};