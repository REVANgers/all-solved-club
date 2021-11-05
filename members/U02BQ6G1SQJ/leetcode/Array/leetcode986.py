class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if ((not firstList) or (not secondList)):
            return [];
        
        (answerList, firstIdx, secondIdx) = ([], 0, 0);
        
        while ((firstIdx < len(firstList)) and (secondIdx < len(secondList))):
            (firstStart, firstEnd) = firstList[firstIdx];
            (secondStart, secondEnd) = secondList[secondIdx];
            
            # print("first :", firstStart, firstEnd);
            # print("second :", secondStart, secondEnd);
            # print();
            
            if (firstStart < secondStart):
                if (secondStart <= firstEnd):
                    answerList.append([secondStart, min(firstEnd, secondEnd)]);
            else:
                if (firstStart <= secondEnd):
                    answerList.append([firstStart, min(firstEnd, secondEnd)]);
            
            if (firstEnd < secondEnd):
                firstIdx += 1;
            else:
                secondIdx += 1;
                
        return answerList;
