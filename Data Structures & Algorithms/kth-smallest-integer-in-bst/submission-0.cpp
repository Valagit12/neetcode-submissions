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
    void dfs(TreeNode* root, int* count, int* res) {
        if (!root) return;

        dfs(root->left, count, res);
        *count -= 1;
        if (*count == 0) {
            *res = root->val;
        }
        dfs(root->right, count, res);
    }
    
    
    int kthSmallest(TreeNode* root, int k) {
        int ans = -1;
        int count = k;
        dfs(root, &count, &ans);
        return ans;
    }

    


};
