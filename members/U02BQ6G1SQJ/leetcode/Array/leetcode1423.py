class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        remainCnt = len(cardPoints) - k;
        curSum = sum(cardPoints[ : remainCnt]);
        minSum = curSum;
        
        # print("remainCnt :", remainCnt);
        
        for startIdx in range(1, k + 1):
            endIdx = startIdx + remainCnt;
            curSum = curSum + cardPoints[endIdx - 1] - cardPoints[startIdx - 1];
            minSum = min(minSum, curSum);
            
            # print("start :", startIdx);
            # print("end :", endIdx);
            # print("curSum :", curSum);
            
        return (sum(cardPoints) - minSum);
