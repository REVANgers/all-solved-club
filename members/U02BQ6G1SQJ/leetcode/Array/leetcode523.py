# reference : https://leetcode.com/problems/continuous-subarray-sum/discuss/236976/Python-solution

# import collections;
# import itertools;

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        if (len(nums) == 1):
            return False;
        
        subarrayList = [];
        
        for numIdx in range(len(nums) - 1):
            subarrayList.append((nums[numIdx] + nums[numIdx + 1]) % k);
        
        numCounter = collections.Counter(map(lambda num : (num % k), itertools.accumulate(subarrayList)));
        
        # print(subarrayList);
        # print(numCounter);
        
        return ((0 in numCounter.keys()) or (numCounter.most_common(1)[0][1] > 1));
        """
    
        (curSum, sumDict) = (0, {0 : -1});
        
        for numIdx in range(len(nums)):
            curSum = (curSum + nums[numIdx]) % k;
                
            if (curSum in sumDict.keys()):
                if (numIdx - sumDict[curSum] >= 2):
                    return True;
            else:
                sumDict[curSum] = numIdx;
                
        return False;
