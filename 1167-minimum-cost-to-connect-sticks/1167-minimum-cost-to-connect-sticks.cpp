class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        int res = 0;

        for (auto i : sticks) minHeap.push(i);

        while (minHeap.size() > 1) {
            int tmp = minHeap.top();
            minHeap.pop();
            int curr = tmp + minHeap.top();
            minHeap.pop();

            minHeap.push(curr);
            res += curr;
        }

        return res;
    }
};