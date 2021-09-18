import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(gridList : List[List[str]], isVisitedList : List[List[bool]], r : int, c : int):
    return ((r < 0) or (r >= len(gridList)) or (c < 0) or (c >= len(gridList[r])) or (isVisitedList[r][c]) or (gridList[r][c] == "0"));
    
def bfs(gridList : List[List[str]], isVisitedList : List[List[bool]], startR : int, startC : int) -> int:
    dq = collections.deque([[startR, startC]]);

    while (dq):
        (curR, curC) = dq.popleft();

        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);

            if (checkImpossible(gridList, isVisitedList, nextR, nextC)):
                continue;

            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);

    return 1;

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        (answer, isVisitedList) = (0, [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]);
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if ((isVisitedList[r][c]) or (grid[r][c] == "0")):
                    continue;
                    
                isVisitedList[r][c] = True;
                answer += bfs(grid, isVisitedList, r, c);
                
        return answer;
