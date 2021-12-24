class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        (answer, left, right) = (len(nums), 0, len(nums) - 1);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            # print(left, mid, right);
            
            if (nums[mid] < target):
                left = mid + 1;
            elif (nums[mid] > target):
                (answer, right) = (mid, mid - 1);
            else:
                return mid;
            
        return answer;
