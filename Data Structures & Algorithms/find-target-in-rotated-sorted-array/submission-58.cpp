class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0; int r = nums.size() - 1;
        
        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] == target) return mid;

            if (nums[l] <= nums[mid] && nums[mid] <= nums[r]) {
                if (nums[mid] > target) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else if (nums[l] <= nums[mid]){
                if (target < nums[l] || target > nums[mid]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                if (target >= nums[l] || target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
};

// [3,4,5,6,1,2] 231
// 
              
