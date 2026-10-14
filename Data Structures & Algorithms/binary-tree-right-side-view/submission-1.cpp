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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if (!root) return ans;

        queue<TreeNode*> queue;
        queue.push(root);

        while (queue.size()) {
            int size = queue.size();
            ans.push_back(queue.front()->val);
            for (int i = 0; i < size; ++i) {
                TreeNode* node = queue.front();

                if (node->right) queue.push(node->right);
                if (node->left) queue.push(node->left);

                queue.pop();
                
            }
        }

        return ans;
    }
};
