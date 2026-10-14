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
    std::vector<int> &A = nums1, &B = nums2;
    if (B.size() < A.size()) std::swap(A, B);

    int n = int(nums1.size() + nums2.size());
    int half = n / 2;
    int l = 0, h = int(A.size()) - 1;

    int Asz = (int)A.size(), Bsz = (int)B.size();

    while (true) {
        int i = (int)std::floor((l + h) / 2.0); // key difference vs Python
        int j = half - i - 2;

        double left_a  = (i >= 0)        ? A[i]       : INT_MIN;
        double right_a = (i + 1 < Asz)   ? A[i + 1]   : INT_MAX;
        double left_b  = (j >= 0)        ? B[j]       : INT_MIN;
        double right_b = (j + 1 < Bsz)   ? B[j + 1]   : INT_MAX;

        if (left_a <= right_b && left_b <= right_a) {
            if (n % 2 == 0) {
                return (std::max(left_a, left_b) + std::min(right_a, right_b)) / 2.0;
            }
            return std::min(right_a, right_b);
        } else if (left_a > right_b) {
            h = i - 1;
        } else {
            l = i + 1;
        }
    }
}
};
