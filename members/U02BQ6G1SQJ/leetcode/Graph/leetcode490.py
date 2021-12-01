import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(mazeList : List[List[int]], isVisitedList : List[List[int]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(mazeList)) or (c < 0) or (c >= len(mazeList[r])) or (mazeList[r][c] == 1));

def getNextPos(mazeList : List[List[int]], isVisitedList : List[List[int]], curR : int, curC : int, dr : int, dc : int) -> Tuple[int]:
    (nextR, nextC) = (curR, curC);
    
    while (True):
        (nextR, nextC) = (nextR + dr, nextC + dc);
        
        if (checkImpossible(mazeList, isVisitedList, nextR, nextC)):
            return (nextR - dr, nextC - dc);
        
    return (curR, curC);

def bfs(mazeList : List[List[int]], startR : int, startC : int, destinationR : int, destinationC : int) -> bool:
    (dq, isVisitedList) = (collections.deque([[startR, startC]]), [[False for _ in range(len(mazeList[0]))] for _ in range(len(mazeList))]);
    isVisitedList[startR][startC] = True;
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        if ((curR, curC) == (destinationR, destinationC)):
            return True;
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = getNextPos(mazeList, isVisitedList, curR, curC, dr, dc);
            
            if ((isVisitedList[nextR][nextC]) or ((nextR, nextC) == (curR, curC))):
                continue;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
        
    return False;

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        return bfs(maze, start[0], start[1], destination[0], destination[1]);
