class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0;
        int right = letters.size() - 1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            if(left == right && right == letters.size() - 1){
                break;
            }

            if(letters[mid] <= target && target < letters[mid + 1]){
                return letters[mid + 1];
            }else if (letters[mid] <= target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return letters[0];

        
    }
};