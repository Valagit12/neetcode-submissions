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
public:
    bool dfs(TreeNode* root, long long left = INT_MIN, long long right = INT_MAX) {
        if (!root) return true;

        if (root->val <= left || root->val >= right) return false;
        return dfs(root->left, left, (long long)root->val) && 
               dfs(root->right, (long long)root->val, right);

    }

    bool isValidBST(TreeNode* root) {   
        return dfs(root);
    }
};

            //     5
            // 4       6
            //      3.    7
