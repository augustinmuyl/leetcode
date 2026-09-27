class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0;

        for (int r = 1; r < nums.size(); ++r) {
            if (nums[r] != nums[l]) {
                nums[l + 1] = nums[r];
                l += 1;
            }
        }

        while (nums.size() > l + 1) nums.pop_back();

        return l + 1;
    }
};