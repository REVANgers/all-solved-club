import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkPosImpossible(gridList : List[List[int]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])));

def checkVisitImpossible(gridList : List[List[int]], isVisitedList : List[List[bool]], r : int, c : int) -> bool:
    return ((isVisitedList[r][c]) or (gridList[r][c] == 0));

def bfs(gridList : List[List[int]], isVisitedList : List[List[bool]], startR : int, startC : int) -> int:
    (areaCnt, dq) = (0, collections.deque([[startR, startC]]));
    
    while (dq):
        (curR, curC) = dq.popleft();
        areaCnt += 1;
        
        # print(areaCnt, curR, curC);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if ((checkPosImpossible(gridList, nextR, nextC)) or (checkVisitImpossible(gridList, isVisitedList, nextR, nextC))):
                continue;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
        
    return areaCnt;

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        (answer, isVisitedList) = (0, [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]);
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (checkVisitImpossible(grid, isVisitedList, r, c)):
                    continue;
                    
                isVisitedList[r][c] = True;
                answer = max(answer, bfs(grid, isVisitedList, r, c));
                
        return answer;
