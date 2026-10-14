class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for (char c : s) {
            if (stack.size() != 0) {
                if (c == ')' && stack.top() == '(') stack.pop();
                else if (c == ']' && stack.top() == '[') stack.pop();
                else if (c == '}' && stack.top() == '{') stack.pop();
                else stack.push(c);
            } else stack.push(c);
        }

        return stack.size() == 0;
    }
};
