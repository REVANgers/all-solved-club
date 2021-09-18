class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalList = sorted(intervals);
        answerList = [intervalList[0]];
        
        # print(intervalList);
        
        for (curStart, curEnd) in intervalList[1 : ]:
            (lastStart, lastEnd) = answerList[-1];
            
            if (curStart > lastEnd):
                answerList.append([curStart, curEnd]);
            else:
                answerList[-1] = [lastStart, max(lastEnd, curEnd)];
        
        return answerList;
