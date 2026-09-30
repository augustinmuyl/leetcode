class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res(matrix.size() * matrix[0].size());
        int i = 0, j = 0, c = 0, b = 0;

        while (true) {
            while (j < matrix[0].size() - b) {
                res[c] = matrix[i][j];
                j++, c++;
            }
            if (c == matrix.size() * matrix[0].size()) break;
            i++, j--;
            while (i < matrix.size() - b) {
                res[c] = matrix[i][j];
                i++, c++;
            }
            if (c == matrix.size() * matrix[0].size()) break;
            j--, i--;
            while (j >= 0 + b) {
                res[c] = matrix[i][j];
                j--, c++;
            }
            if (c == matrix.size() * matrix[0].size()) break;
            b++, j++, i--;
            while (i >= 0 + b) {
                res[c] = matrix[i][j];
                i--, c++;
            }
            if (c == matrix.size() * matrix[0].size()) break;
            i++, j++;
        }

        return res;
    }
};