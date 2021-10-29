import collections;

MOD = 60;

def getPairCnt(timeCntList : List[int], timeIdx : int) -> int:
    return ((timeCntList[timeIdx] * (timeCntList[timeIdx] - 1)) // 2);

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        (answer, left, right, timeCntList) = (0, 1, MOD - 1, [0 for _ in range(MOD)]);
        
        for curTime in time:
            timeCntList[curTime % MOD] += 1;
            
        # print(timeCntList);
        
        while (left < right):
            answer += (timeCntList[left] * timeCntList[right]);
            (left, right) = (left + 1, right - 1);
            
        # print(answer);
            
        return (answer + getPairCnt(timeCntList, 0) + getPairCnt(timeCntList, MOD // 2));
