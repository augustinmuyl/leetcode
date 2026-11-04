class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> res;

        for (const auto& word : strs) {
            string sorted = word;
            sort(sorted.begin(), sorted.end());

            map[sorted].push_back(word);
        }

        for (auto& pair : map) res.push_back(pair.second);

        return res;
    }
};