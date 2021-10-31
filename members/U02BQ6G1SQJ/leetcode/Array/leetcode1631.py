import heapq;
import math;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def getNextEffort(heightList : List[List[int]], visitList : List[List[int]], curR : int, curC : int, curEffort : int, nextR : int, nextC : int) -> int:
    if ((nextR < 0) or (nextR >= len(heightList)) or (nextC < 0) or (nextC >= len(heightList[nextR]))):
        return -1;
    
    nextEffort = max(curEffort, (abs(heightList[nextR][nextC] - heightList[curR][curC])));
    return (nextEffort if (visitList[nextR][nextC] > nextEffort) else -1);

def bfs(heightList : List[List[int]], startR : int, startC : int, endR : int, endC : int) -> int:
    (pq, visitList) = ([[startR, startC, 0]], [[math.inf for _ in range(len(heightList[0]))] for _ in range(len(heightList))]);
    visitList[startR][startC] = 0;
    
    while (pq):
        (curR, curC, curEffort) = heapq.heappop(pq);
        
        if ((curR, curC) == (endR, endC)):
            return curEffort;
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            nextEffort = getNextEffort(heightList, visitList, curR, curC, curEffort, nextR, nextC);
            
            if (nextEffort == -1):
                continue;
            
            visitList[nextR][nextC] = nextEffort;
            heapq.heappush(pq, [nextR, nextC, nextEffort]);
    
    return -1;

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return bfs(heights, 0, 0, len(heights) - 1, len(heights[-1]) - 1);
