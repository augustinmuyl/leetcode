class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int curr = nums[0], count = 0;

        for (auto i : nums) {
            if (count == 0) curr = i;
            if (i == curr) count++;
            else count--;
        }

        return curr;
    }
};