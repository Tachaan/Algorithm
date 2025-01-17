class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 1;
        int right = nums.size() - 1;
        
        if (nums[0] < nums[right]){
            return nums[0];
        }

        while(left<=right){
            int mid = left + (right - left) / 2;

            if(nums[mid - 1] > nums[mid]){
                return nums[mid];
            }
            
            if(nums[left] < nums[mid] && nums[mid] < nums[right]){
                right = mid - 1;
            }else{
                if(nums[left] > nums[mid]){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }

        }
        return nums[0];
    }
};