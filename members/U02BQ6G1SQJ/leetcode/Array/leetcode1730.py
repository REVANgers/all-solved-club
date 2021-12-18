import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def findStartPos(gridList : List[List[str]]):
    for r in range(len(gridList)):
        for c in range(len(gridList[r])):
            if (gridList[r][c] == '*'):
                return [r, c];
            
    return [-1, -1];

def checkImpossible(gridList : List[List[str]], isVisitedList : List[List[bool]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])) or (isVisitedList[r][c]) or (gridList[r][c] == 'X'));

def bfs(gridList : List[List[str]], startR : int, startC : int) -> int:
    (dq, isVisitedList) = (collections.deque([[startR, startC, 0]]), [[False for _ in range(len(gridList[0]))] for _ in range(len(gridList))]);
    
    while (dq):
        (curR, curC, curDist) = dq.popleft();
        
        if (gridList[curR][curC] == "#"):
            return curDist;
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(gridList, isVisitedList, nextR, nextC)):
                continue;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC, curDist + 1]);
    
    return -1;

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        (startR, startC) = findStartPos(grid);            
        
        # print(startR, startC);
        
        return bfs(grid, startR, startC);
