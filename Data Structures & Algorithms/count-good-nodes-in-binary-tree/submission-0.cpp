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
    int dfs(TreeNode* root, int maxval) {
        if (!root) return 0;

        int count = (root->val >= maxval) ? 1 : 0;

        maxval = max(root->val, maxval);

        count += dfs(root->left, maxval);
        count += dfs(root->right, maxval);

        return count;
    }

    int goodNodes(TreeNode* root) {
        if (!root) return 0;

        return dfs(root, root->val);
    }
};


/*
               
               3
          3.      

    4       2




*/

