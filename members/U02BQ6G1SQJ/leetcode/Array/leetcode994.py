import collections;
import math;

(IMPOSSIBLE, EMPTY_CELL, FRESH_ORANGE, ROTTEN_ORANGE, DIR_VEC) = (-1, 0, 1, 2, ((-1, 0), (1, 0), (0, -1), (0, 1)));

def checkImpossible(gridList : List[List[int]], visitList : List[List[int]], curR : int, curC : int, nextR : int, nextC : int, nextTime : int) -> bool:
    return ((nextR < 0) or (nextR >= len(gridList)) or (nextC < 0) or (nextC >= len(gridList[nextR])) or (gridList[nextR][nextC] == EMPTY_CELL) or (visitList[nextR][nextC] <= nextTime));

def bfs(gridList : List[List[int]], visitList : List[List[int]], startR : int, startC : int) -> None:
    (visitList[startR][startC], dq) = (0, collections.deque([[startR, startC, 0]]));
    
    while (dq):
        (curR, curC, curTime) = dq.popleft();
        
        # print(curR, curC, curTime);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC, nextTime) = (curR + dr, curC + dc, curTime + 1);
            
            if (checkImpossible(gridList, visitList, curR, curC, nextR, nextC, nextTime)):
                continue;
                
            (gridList[nextR][nextC], visitList[nextR][nextC]) = (ROTTEN_ORANGE, nextTime);
            dq.append([nextR, nextC, nextTime]);
        
    return None;

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        (answer, startList, visitList) = (0, [], [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]);
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (grid[r][c] == ROTTEN_ORANGE):
                    startList.append([r, c]);
        
        for (r, c) in startList:
            bfs(grid, visitList, r, c);
            
            # print(visitList);
                
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (visitList[r][c] == math.inf):
                    if (grid[r][c] == FRESH_ORANGE):
                        return IMPOSSIBLE;
                else:
                    answer = max(answer, visitList[r][c]);
                
        return (answer if (startList) else 0);
