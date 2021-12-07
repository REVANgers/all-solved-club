import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(gridList : List[List[int]], isVisitedList : List[List[bool]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])) or (isVisitedList[r][c]) or (gridList[r][c] == 1));

def checkBoundary(gridList : List[List[int]], r : int, c : int) -> bool:
    return ((r in [0, len(gridList) - 1]) or (c in [0, len(gridList[r]) - 1]));

def bfs(gridList : List[List[int]], isVisitedList : List[List[bool]], startR : int, startC : int) -> int:
    (result, dq) = (1, collections.deque([[startR, startC]]));
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        for (dr, dc) in (DIR_VEC):
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(gridList, isVisitedList, nextR, nextC)):
                continue;
            
            if ((checkBoundary(gridList, nextR, nextC)) and (gridList[nextR][nextC] == 0)):
                result = 0;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
            
    return result;

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        (answer, isVisitedList) = (0, [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]);
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if ((checkBoundary(grid, r, c)) or (isVisitedList[r][c]) or (grid[r][c] == 1)):
                    continue;
                    
                isVisitedList[r][c] = True;
                answer += bfs(grid, isVisitedList, r, c);
                
        return answer;
