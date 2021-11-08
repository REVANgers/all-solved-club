import collections;

DIR_VEC = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1));

def checkImpossible(gridList : List[List[int]], isVisitedList : List[List[bool]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])) or (isVisitedList[r][c]) or (gridList[r][c] == 1));

def bfs(gridList : List[List[int]], startR : int, startC : int, endR : int, endC : int) -> int:
    if (gridList[startR][startC] == 1):
        return -1;
    
    (dq, isVisitedList) = (collections.deque([[startR, startC, 1]]), [[False for _ in range(len(gridList[0]))] for _ in range(len(gridList))]);
    isVisitedList[startR][startC] = True;
    
    # print("start :", startR, startC);
    # print("end :", endR, endC);
    
    while (dq):
        (curR, curC, curDist) = dq.popleft();

        # print("cur :", curR, curC, curDist);
        
        if ((curR, curC) == (endR, endC)):
            return curDist;
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(gridList, isVisitedList, nextR, nextC)):
                continue;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC, curDist + 1]);
            
    return -1;

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return bfs(grid, 0, 0, len(grid) - 1, len(grid[-1]) - 1);
