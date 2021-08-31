import heapq;
import math;

(STRAIGHT_COST, CORNER_COST) = (100, 500);
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(boardList : list, r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(boardList)) or (c < 0) or (c >= len(boardList[r])) or (boardList[r][c] != 0));

def addCost(curDir : int, nextDir : int) -> int:
    if (curDir == -1):
        return STRAIGHT_COST;
    
    return (STRAIGHT_COST if (curDir == nextDir) else (STRAIGHT_COST + CORNER_COST));
    
def bfs(boardList : list) -> int:
    (startPos, endPos) = ([0, 0], [len(boardList) - 1, len(boardList[len(boardList) - 1]) - 1]);
    (pq, visitList) = ([[0, -1] + startPos], [[[math.inf for _ in range(endPos[1] + 1)] for _ in range(endPos[0] + 1)] for _ in range(len(DIR_VEC))]);
    
    while (pq):
        (curCost, curDir, curR, curC) = heapq.heappop(pq);
        
        # print(curCost, curDir, curR, curC);
        
        if ([curR, curC] == endPos):
            return curCost;
        
        for nextDir in range(len(DIR_VEC)):
            (dr, dc) = DIR_VEC[nextDir];
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(boardList, nextR, nextC)):
                continue;
                
            nextCost = curCost + addCost(curDir, nextDir);
            
            if (visitList[nextDir][nextR][nextC] <= nextCost):
                continue;
                
            visitList[nextDir][nextR][nextC] = nextCost;
            heapq.heappush(pq, [nextCost, nextDir, nextR, nextC]);
            
    return 0;

def solution(board : list) -> int: 
    return bfs(board);
