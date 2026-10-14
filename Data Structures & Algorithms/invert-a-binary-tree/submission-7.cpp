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
    TreeNode* invertTree(TreeNode* root) {
        //DFS recursive
        // if (!root) return nullptr;

        // if (root->left)
        //     invertTree(root->left);
        // if (root->right)
        //     invertTree(root->right);
        
        // swap(root->left, root->right);  
        // return root;

        //BFS recursive
        // if (!root) return nullptr;
        // swap(root->left, root->right);

        // if (root->left)
        //     invertTree(root->left);
        
        // if (root->right)
        //     invertTree(root->right);
        
        // return root;

        //Iterative DFS
        // if (!root) return nullptr;
        // stack<TreeNode*> stack;
        // stack.push(root);

        // while (stack.size()) {
        //     TreeNode* node = stack.top(); stack.pop();

        //     swap(node->left, node->right);

        //     if (node->left) stack.push(node->left);
        //     if (node->right)stack.push(node->right);
        // }

        // return root;
        
        // Iterative BFS
        if (!root) return nullptr;
        queue<TreeNode*> queue;
        queue.push(root);

        while (queue.size()) {
            TreeNode* node = queue.front(); queue.pop();

            swap(node->left, node->right);
            if (node->left) queue.push(node->left);
            if (node->right) queue.push(node->right);
        }
        return root;

    }
};
