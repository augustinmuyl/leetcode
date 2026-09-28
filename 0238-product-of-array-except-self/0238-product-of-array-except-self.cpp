class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);
        int l = 1, r = nums.size() - 2;
        int p = 1, s = 1;

        while (l < nums.size() && r >= 0) {
            p *= nums[l - 1];
            s *= nums[r + 1];

            res[l] *= p, res[r] *= s;

            l++, r--;
        }

        return res;
    }
};