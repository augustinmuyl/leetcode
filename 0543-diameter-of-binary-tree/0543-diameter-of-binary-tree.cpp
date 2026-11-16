/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int dfs(TreeNode* node, int &max_diam) {
        if (node == nullptr)
            return 0;
        
        int l = dfs(node->left, max_diam);
        int r = dfs(node->right, max_diam);

        max_diam = max(max_diam, l + r);

        return 1 + max(l, r);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diam = 0;

        dfs(root, max_diam);

        return max_diam;
    }
};