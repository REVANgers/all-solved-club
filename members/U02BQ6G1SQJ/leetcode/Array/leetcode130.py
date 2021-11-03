import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkPos(boardList : List[List[str]], isVisitedList : List[List[bool]], r : int, c : int) -> int:
    if ((r < 0) or (r >= len(boardList)) or (c < 0) or (c >= len(boardList[r]))):
        return -1;
    
    if ((isVisitedList[r][c]) or (boardList[r][c] == "X")):
        return 0;
    
    return 1;

def bfs(boardList : List[List[str]], isVisitedList : List[List[bool]], startR : int, startC : int) -> List[List[int]]:
    (posList, isFilp, isVisitedList[startR][startC], dq) = ([], True, True, collections.deque([[startR, startC]]));
    
    while (dq):
        (curR, curC) = dq.popleft();
        posList.append([curR, curC]);
        
        # print(curR, curC);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            checkResult = checkPos(boardList, isVisitedList, nextR, nextC);
            
            # print(checkResult);
            
            if (checkResult == -1):
                isFilp = False;
                continue;
            elif (checkResult == 0):
                continue;
                
            isVisitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
    
    return (posList if (isFilp) else []);

def filpPos(boardList : List[List[str]], posList : List[List[int]]) -> None:
    for (r, c) in posList:
        boardList[r][c] = "X";
        
    return None;
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        isVisitedList = [[False for _ in range(len(board[0]))] for _ in range(len(board))];
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (isVisitedList[r][c]) or (board[r][c] == "X"):
                    continue;
                
                posList = bfs(board, isVisitedList, r, c);
                
                # print(posList);
                
                if (posList):
                    filpPos(board, posList);
                
        return None;
