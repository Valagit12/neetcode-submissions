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
    int maxDepth( TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> queue;
        queue.push(root);

        int depth = 0;
        while(queue.size()) {
            int size = queue.size();

            for (int i = 0; i < size; ++i) {
                TreeNode* node = queue.front(); queue.pop();

                if (node->left) queue.push(node->left);
                if (node->right) queue.push(node->right);
            }
            ++depth;
        }
        return depth;
    }
};
