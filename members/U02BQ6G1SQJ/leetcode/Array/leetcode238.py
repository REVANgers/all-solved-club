import itertools;
import operator;

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if (len(nums) == 1):
            return nums;
        
        (answerList, prefixMulList, suffixMulList) = ([], list(itertools.accumulate(nums, operator.mul)), list(itertools.accumulate(nums[ : : -1], operator.mul))[ : : -1]);
        (prefixMulIdx, suffixMulIdx) = (0, 1);
        
        # print(prefixMulList);
        # print(suffixMulList);
        # print();
        
        answerList.append(suffixMulList[suffixMulIdx]);
        suffixMulIdx += 1;
        
        for numIdx in range(1, len(nums) - 1):
            answerList.append(prefixMulList[prefixMulIdx] * suffixMulList[suffixMulIdx]);
            (prefixMulIdx, suffixMulIdx) = (prefixMulIdx + 1, suffixMulIdx + 1);
            
        answerList.append(prefixMulList[prefixMulIdx]);
        prefixMulIdx += 1;
        return answerList;
