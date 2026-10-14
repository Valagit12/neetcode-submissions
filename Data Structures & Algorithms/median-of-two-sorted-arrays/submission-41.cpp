class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        /*
        A - [1 3 7 7]

        B - [2 4 5 6 8]

        1 2 3 4 5 6 6 7 7 8

        mid = A[1] -> 2 elements in Aleft.
                   -> 3 elements in Bleft
                        10 - half = 5 - 2 = 3. -> half - i - 2


        */
        std::vector<int> &A = nums1; std::vector<int> &B = nums2;
        if (B.size() < A.size()) swap(A, B);
        int n = nums1.size() + nums2.size();
        int half = n / 2;
        int l = 0; int h = A.size() - 1;

        while (true) {
            int i = (int)floor((l+h) / 2.0);
            int j = half - i - 2;

            double left_a = (i >= 0) ? A[i] : INT_MIN;
            double right_a = (i < (int)A.size() - 1) ? A[i + 1] : INT_MAX;
            double left_b = (j >= 0) ? B[j] : INT_MIN;
            double right_b = (j + 1 < (int)B.size()) ? B[j + 1] : INT_MAX;

            if (left_a <= right_b && left_b <= right_a) {
                if (n % 2 == 0) {
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2;
                }
                return min(right_a, right_b);
            } else if (left_a > right_b) h = i - 1;
            else l = i + 1;
        
        }
        return -1;
    }
};
