class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<char> stack;
        std::vector<string> result;

        backtrack(0, 0, n, result, stack);
        return result;
    }

    void backtrack(int openN, int closedN, int n, vector<string> &res, vector<char> &stack) {
        if (openN == closedN && closedN == n) {
            res.emplace_back(std::string(stack.begin(), stack.end()));
            return;
        }

        if (openN < n) {
            stack.push_back('(');
            backtrack(openN + 1, closedN,n, res, stack);
            stack.pop_back();
        }
        if (closedN < openN) {
            stack.push_back(')');
            backtrack(openN, closedN + 1, n, res, stack);
            stack.pop_back();
        }
    }
};
