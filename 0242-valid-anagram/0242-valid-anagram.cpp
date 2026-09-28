class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> charMap;

        for (const auto& i : s) charMap[i]++;
        for (const auto& i : t) charMap[i]--;

        for (const auto& i : charMap) {
            if (i.second != 0) return false;
        }

        return true;
    }
};