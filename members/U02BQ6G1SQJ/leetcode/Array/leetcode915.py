import collections;

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        (answer, rightCounter) = (0, collections.Counter(nums));
        (leftMax, rightMin) = (-1, min(rightCounter.keys()));
        
        for numIdx in range(len(nums)):
            (leftMax, rightCounter[nums[numIdx]]) = (max(leftMax, nums[numIdx]), rightCounter[nums[numIdx]] - 1);
            
            if (rightCounter[nums[numIdx]] == 0):
                del rightCounter[nums[numIdx]];
                
                if (rightMin == nums[numIdx]):
                    rightMin = min(rightCounter.keys());
            
            # print(leftMax, rightMin);
            
            if (leftMax <= rightMin):
                return (numIdx + 1);
        
        # print(leftCounter);
        # print(rightCounter);
        
        return -1;
