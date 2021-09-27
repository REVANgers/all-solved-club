import itertools;
import collections;

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        answer = 0;
        
        for startIdx in range(len(nums)):
            curSum = 0;
            
            for endIdx in range(startIdx, len(nums)):
                curSum += nums[endIdx];
                
                if (curSum == k):
                    answer += 1;
                    
        return answer;
        """
        
        """
        prefixSumList = list(itertools.accumulate(nums));
        (answer, totalSum) = (0, prefixSumList[-1]);
        
        # print(prefixSumList);
        # print(totalSum);
        
        for startIdx in range(len(nums)):
            for endIdx in range(startIdx, len(nums)):
                startSum = (0 if (startIdx == 0) else prefixSumList[startIdx - 1]);
                endSum = prefixSumList[endIdx];
                
                if (endSum - startSum == k):
                    answer += 1;
                    
        return answer;
        """
        
        (answer, curSum, sumDict) = (0, 0, collections.defaultdict(int));
        sumDict[0] = 1;
        
        for curNum in nums:
            curSum += curNum;
            
            if (curSum - k in sumDict):
                answer += sumDict[curSum - k];
                
            sumDict[curSum] += 1;
            
        return answer;
        
