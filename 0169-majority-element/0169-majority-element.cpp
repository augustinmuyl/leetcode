class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int curr = nums[0], count = 0;

        for (auto i : nums) {
            if (i == curr) count++;
            else if (count == 0) count++, curr = i;
            else if (count-- == 0) curr = i;
        }

        return curr;
    }
};