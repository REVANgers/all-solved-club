import collections;

class Solution:
    def numSplits(self, s: str) -> int:
        (answer, leftCounter, rightCounter) = (0, collections.Counter(), collections.Counter(s));
        
        for curCh in s:
            (leftCounter[curCh], rightCounter[curCh]) = (leftCounter[curCh] + 1, rightCounter[curCh] - 1);
            
            if (rightCounter[curCh] == 0):
                del rightCounter[curCh];
            
            if (len(leftCounter) == len(rightCounter)):
                answer += 1;
            
            # print(leftCounter);
            # print(rightCounter);
            # print();
            
        return answer;
