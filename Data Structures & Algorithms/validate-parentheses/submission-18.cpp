class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for (char c : s) {
            if (stack.size() != 0) {
                if ((c == ')' && stack.top() == '(') || (c == ']' && stack.top() == '[') || (c == '}' && stack.top() == '{')) {
                    stack.pop();
                    continue;
                } 
            }
            stack.push(c);
        }

        return stack.size() == 0;
    }
};
