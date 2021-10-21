import math;

CHANGE_CNT = 3;

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if (len(nums) <= CHANGE_CNT + 1):
            return 0;
        
        (answer, sortedNumList) = (math.inf, sorted(nums));
        
        for left in range(len(sortedNumList)):
            right = len(sortedNumList) - CHANGE_CNT + left - 1;
            
            if (right == len(sortedNumList)):
                break;
                
            # print(left, right);
            
            answer = min(answer, sortedNumList[right] - sortedNumList[left]);
            
        return answer;
