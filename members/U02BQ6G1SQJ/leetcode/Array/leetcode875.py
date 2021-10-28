def checkPossible(pileList: List[int], h: int, speed : int) -> bool:
    curTime = 0;
    
    for curPile in pileList:
        curTime += math.ceil(curPile / speed);
        
        if (curTime > h):
            return False;
        
    return True;

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        (answer, left, right) = (1, 1, max(piles));
        
        while (left <= right):
            mid = (left + right) // 2;
            
            if (checkPossible(piles, h, mid)):
                (answer, right) = (mid, mid - 1);
            else:
                left = mid + 1;
        
        return answer;
