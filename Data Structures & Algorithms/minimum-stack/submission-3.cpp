#include <stack>
#include <climits>

class MinStack {
private:
    std::stack<long long> st;   // store differences as 64-bit
    long long currMin = LLONG_MAX;

public:
    void push(int val) {
        long long v = val;
        if (st.empty()) {
            st.push(0);         // v - v
            currMin = v;
        } else {
            st.push(v - currMin);  // may be negative, may be > INT_MAX
            if (v < currMin) currMin = v;
        }
    }

    void pop() {
        if (st.empty()) return;
        long long diff = st.top();
        st.pop();
        if (diff < 0) {
            // top was the current min; restore previous min
            currMin = currMin - diff; // oldMin = currMin - (v - oldMin)
        }
        if (st.empty()) currMin = LLONG_MAX; // reset
    }

    int top() {
        if (st.empty()) return 0; // or throw
        long long diff = st.top();
        long long v = (diff < 0) ? currMin : (currMin + diff);
        return static_cast<int>(v);
    }

    int getMin() {
        return st.empty() ? 0 : static_cast<int>(currMin); // or throw if empty
    }
};
