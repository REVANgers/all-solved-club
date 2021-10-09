import math;

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if (not intervals):
            return [newInterval];
        
        (answerList, left, right) = ([], math.inf, -1);
        
        for intervalIdx in range(len(intervals)):
            (start, end) = intervals[intervalIdx];
            
            # print(start, end);
                
            if (start > newInterval[1]):
                break;
                
            if (end < newInterval[0]):
                continue;
                
            (left, right) = (min(left, intervalIdx), max(right, intervalIdx));
                
        # print(left, right);
        
        if (right == -1):
            isInserted = False;
            
            for intervalIdx in range(len(intervals)):
                (start, end) = intervals[intervalIdx];
                
                if ((isInserted) or (start < newInterval[0])):
                    answerList.append([start, end]);
                else:
                    isInserted = True;
                    answerList.extend([newInterval, [start, end]]);
                    
            if (not isInserted):
                answerList.append(newInterval);
                
        else:
            for intervalIdx in range(left):
                answerList.append(intervals[intervalIdx]);

            answerList.append([min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]);

            for intervalIdx in range(right + 1, len(intervals)):
                answerList.append(intervals[intervalIdx]);
            
        return answerList;
