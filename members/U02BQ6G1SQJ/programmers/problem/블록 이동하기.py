import heapq;
import math;

(START_TIME, START_DIR, START_R1, START_C1, START_R2, START_C2) = (0, 1, 0, 0, 0, 1);
MOVE_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));
ROTATE_VEC = (
    ((3, 1, -1, 0, 0), (3, 0, 0, -1, 1), (2, -1,  -1, 0, 0), (2, 0, 0, 1, 1)), 
    ((1, -1, 1, 0, 0), (1, 0, 0, 1, -1), (2, 1, 1, 0, 0), (2, 0, 0, -1, -1)), 
    ((-2, 1, 1, 0, 0), (-2, 0, 0, -1, -1), (-1, 1, -1, 0, 0), (-1, 0, 0, -1, 1)), 
    ((-2, -1, -1, 0, 0), (-2, 0, 0, 1, 1), (-3, -1, 1, 0, 0), (-3, 0, 0, 1, -1))
);

def checkMoveImpossible(boardList : list, nextR : int, nextC : int) -> bool:
    return ((nextR < 0) or (nextR >= len(boardList)) or (nextC < 0) or (nextC >= len(boardList[nextR])) or (boardList[nextR][nextC] != 0));

def checkRotateImpossible(boardList : list, curR : int, curC : int, nextR : int, nextC : int) -> bool:
    return ((nextR < 0) or (nextR >= len(boardList)) or (nextC < 0) or (nextC >= len(boardList[nextR])) or (boardList[nextR][nextC] != 0) or (boardList[curR][nextC] != 0) or (boardList[nextR][curC] != 0));

def checkFinished(boardList : list, curR : int, curC : int) -> bool:
    return ((curR == len(boardList) - 1) and (curC == len(boardList[curR]) - 1));

def setNextPos(boardList : list, pq : list, visitList : list, nextTime : int, nextDir : int, nextR1 : int, nextC1 : int, nextR2 : int, nextC2 : int) -> None:
    # print("nextTime :", nextTime, "nextDir :", nextDir);
    # print("next1 :", nextR1, nextC1, "next2 :", nextR2, nextC2);

    if (visitList[nextDir][nextR1][nextC1] <= nextTime):
        # print("CASE 2");
        
        return None;

    visitList[nextDir][nextR1][nextC1] = nextTime;
    heapq.heappush(pq, [nextTime, nextDir, nextR1, nextC1, nextR2, nextC2]);
    
    # print("CASE 0");
    
    return None;

def bfs(boardList : list) -> int:
    pq = [[START_TIME, START_DIR, START_R1, START_C1, START_R2, START_C2]];
    visitList = [[[math.inf for _ in range(len(boardList[0]))] for _ in range(len(boardList))] for _ in range(len(ROTATE_VEC))];
    visitList[START_DIR][START_R1][START_C1] = 0;
    
    while (pq):
        (curTime, curDir, curR1, curC1, curR2, curC2) = heapq.heappop(pq);
        
        # print();
        # print("curTime :", curTime, "curDir :", curDir);
        # print("cur1 :", curR1, curC1, "cur2 :", curR2, curC2);
        # print();
        
        if (checkFinished(boardList, curR1, curC1) or (checkFinished(boardList, curR2, curC2))):
            return curTime;
        
        for (dr, dc) in MOVE_VEC:
            # print(dr, dc);
            
            (nextTime, nextDir, nextR1, nextC1, nextR2, nextC2) = (curTime + 1, curDir, curR1 + dr, curC1 + dc, curR2 + dr, curC2 + dc);
            
            if ((checkMoveImpossible(boardList, nextR1, nextC1)) or (checkMoveImpossible(boardList, nextR2, nextC2))):
                # print("CASE 1");

                continue;
            
            setNextPos(boardList, pq, visitList, nextTime, nextDir, nextR1, nextC1, nextR2, nextC2);
        
        # print(ROTATE_VEC[curDir]);
        
        for (ddir, dr1, dc1, dr2, dc2) in ROTATE_VEC[curDir]:
            # print(ddir, dr1, dc1, dr2, dc2);
            
            (nextTime, nextDir, nextR1, nextC1, nextR2, nextC2) = (curTime + 1, curDir + ddir, curR1 + dr1, curC1 + dc1, curR2 + dr2, curC2 + dc2);
            
            if ((checkRotateImpossible(boardList, curR1, curC1, nextR1, nextC1)) or (checkRotateImpossible(boardList, curR2, curC2, nextR2, nextC2))):
                # print("CASE 1");

                continue;
            
            setNextPos(boardList, pq, visitList, nextTime, nextDir, nextR1, nextC1, nextR2, nextC2);
            
    return -1;

def solution(board : list) -> int:
    return bfs(board);
