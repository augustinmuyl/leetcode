class MinStack {
private:
    stack<int> input, min;

public:
    MinStack() : input(), min() {}

    void push(int value) {
        input.push(value);
        if (min.empty() || min.top() > value) min.push(value);
        else min.push(min.top());
    }

    void pop() {
        input.pop();
        min.pop();
    }

    int top() { return input.top(); }

    int getMin() { return min.top(); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */