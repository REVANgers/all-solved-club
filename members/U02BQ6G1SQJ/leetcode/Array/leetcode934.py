import collections;
import math;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkFirstImpossible(gridList : List[List[int]], visitList : List[List[bool]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])) or (gridList[r][c] == 0) or (visitList[r][c] != math.inf));

def checkSecondImpossible(gridList : List[List[int]], visitList : List[List[bool]], r : int, c : int, dist : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])));

def firstBFS(gridList : List[List[int]], visitList : List[List[bool]], startR : int, startC : int) -> None:
    dq = collections.deque([[startR, startC]]);
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkFirstImpossible(gridList, visitList, nextR, nextC)):
                continue;
                
            visitList[nextR][nextC] = -1;
            dq.append([nextR, nextC]);
        
    return None;

def secondBFS(gridList : List[List[int]], visitList : List[List[bool]], startR : int, startC : int) -> int:
    dq = collections.deque([[startR, startC, 0]]);
    
    while (dq):
        (curR, curC, curDist) = dq.popleft();
        
        # print(curR, curC, curDist);
        # print(visitList);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC, nextDist) = (curR + dr, curC + dc, curDist + 1);
            
            if (checkSecondImpossible(gridList, visitList, nextR, nextC, nextDist)):
                continue;
                
            if (gridList[nextR][nextC] == 1):
                if (visitList[nextR][nextC] == -1):
                    return curDist;
                elif (visitList[nextR][nextC] == -2):
                    continue;
            else:    
                if (visitList[nextR][nextC] <= nextDist):
                    continue;

                visitList[nextR][nextC] = nextDist;
                dq.append([nextR, nextC, nextDist]);
        
    return math.inf;

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        (answer, bfsCnt, visitList) = (math.inf, 0, [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]);
    
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # print(r, c, grid[r][c], visitList[r][c]);
                
                if ((grid[r][c] == 0) or (visitList[r][c] not in (math.inf, -2))):
                    continue;

                if (bfsCnt == 0):
                    (bfsCnt, visitList[r][c]) = (1, -1);
                    firstBFS(grid, visitList, r, c);
                elif (bfsCnt == 1):
                    visitList[r][c] = -2;
                    answer = min(answer, secondBFS(grid, visitList, r, c));

                    # print(visitList);
                    
        return answer;
