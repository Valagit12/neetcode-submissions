class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        /*
        m = ROWS
        n = COLUMNS
        i = 1, j = 1 -> (6 or 7)
        (i * col) + j = mid

        mid = 4, row = 4/ 3 = 1, col = 4 - (1 * 4) = 0
        mid = 5, row = 5 /3 = 1. col = 5 - (1 * 4) = 1
        mid = 7, row = 7 / 3 = 1 col = 7 - (1 * 4) = 3
        */

        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        int ELEMS = ROWS * COLS;

        int l = 0;
        int h = ELEMS - 1;

        int i = 0;
        while (l <= h) {
            // i++;
            // if (i == 3) {
            //     std::cout << (l + h) / 2;
            //     break;
            // }
            int mid = (l + h) / 2;
            int midi = mid / COLS;
            int midj = mid - (midi * COLS);

            int num = matrix[midi][midj];
            std::cout << mid << '\n';
            if (num == target) {
                return true;
            } else if (target > num) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }
        return false;

    }
};
