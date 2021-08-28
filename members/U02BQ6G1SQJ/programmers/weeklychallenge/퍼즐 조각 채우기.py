import collections;
import copy;

ROTATE_CNT = 4;
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

answer = 0;

def checkInvalidPos(matrix : list, visitedList : list, target : int, r : int, c : int) -> bool:
    # print(matrix[r][c], target, visitedList[r][c]);
    
    return (matrix[r][c] != target) or (visitedList[r][c]);

def bfs(matrix : list, visitedList : list, target : int, startR : int, startC : int) -> list:
    puzzleList = [];
    dq = collections.deque([[startR, startC]]);
    
    while (dq):
        (curR, curC) = dq.popleft();
        puzzleList.append([curR, curC]);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            # print(nextR, nextC);
            
            if ((nextR < 0) or (nextR >= len(matrix)) or (nextC < 0) or (nextC >= len(matrix[curR]))):
                continue;
                
            if (checkInvalidPos(matrix, visitedList, target, nextR, nextC)):
                continue;
                
            visitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
    
    # print(puzzleList);
    
    return puzzleList;

def setPuzzleList(matrix : list, puzzleList : list, visitedList : list, target : int) -> None:
    for curR in range(len(matrix)):
        for curC in range(len(matrix[curR])):
            if checkInvalidPos(matrix, visitedList, target, curR, curC):
                continue;
                
            visitedList[curR][curC] = True;
            puzzleList.append(bfs(matrix, visitedList, target, curR, curC));
            
    return None;
    
def checkFill(gameBoardList : list, tableList : list) -> int:
    (rDiff, cDiff) = (tableList[0][0] - gameBoardList[0][0], tableList[0][1] - gameBoardList[0][1]);
    
    # print(gameBoardList);
    # print(tableList);
    
    for tableIdx in range(1, len(tableList)):
        # print(rDiff, cDiff, tableList[tableIdx][0] - gameBoardList[tableIdx][0], tableList[tableIdx][1] - gameBoardList[tableIdx][1]);
        
        if ((rDiff, cDiff) != (tableList[tableIdx][0] - gameBoardList[tableIdx][0], tableList[tableIdx][1] - gameBoardList[tableIdx][1])):
            return 0;
        
    # print(len(gameBoardList));
    
    return len(gameBoardList);
    
def sortPosList(posList : list) -> list:
    return sorted(posList, key = lambda k : (k[0], k[1]));
    
def rotatePosList(posList : list) -> list:
    return [[-c, r] for (r, c) in posList];
    
def getFillCnt(gameBoardList : list, tableList : list) -> int:
    if (len(gameBoardList) != len(tableList)):
        return 0;
    
    (newGameBoardList, newTableList) = (sortPosList(gameBoardList), copy.deepcopy(tableList));
    
    for rotateIdx in range(ROTATE_CNT):
        # print(newGameBoardList);
        # print(newTableList);
        
        fillCnt = checkFill(newGameBoardList, sortPosList(newTableList));
        
        if (fillCnt > 0):
            return fillCnt;

        newTableList = rotatePosList(newTableList);
    
    return 0;

def getAnswer(gameBoardPuzzleList : list, tablePuzzleList : list) -> int:
    answer = 0;
    gameBoardVisitList = [-1 for _ in range(len(gameBoardPuzzleList))];
    
    for tablePuzzleIdx in range(len(tablePuzzleList)):
        for gameBoardPuzzleIdx in range(len(gameBoardPuzzleList)):
            if (gameBoardVisitList[gameBoardPuzzleIdx] != -1):
                continue;
            
            fillCnt = getFillCnt(gameBoardPuzzleList[gameBoardPuzzleIdx], tablePuzzleList[tablePuzzleIdx]);
            
            if (fillCnt > 0):
                gameBoardVisitList[gameBoardPuzzleIdx] = tablePuzzleIdx;
                answer += fillCnt;
                break;
            
    # print(gameBoardVisitList);
            
    return answer;

def solution(game_board : list, table : list) -> int:
    gameBoardPuzzleList = [];
    gameBoardVisitedList = [[False for _ in range(len(game_board[0]))] for _ in range(len(game_board))];
    tablePuzzleList = [];
    tableVisitedList = [[False for _ in range(len(table[0]))] for _ in range(len(table))];
    
    setPuzzleList(game_board, gameBoardPuzzleList, gameBoardVisitedList, 0);
    setPuzzleList(table, tablePuzzleList, tableVisitedList, 1);
    
    # print(len(gameBoardPuzzleList), len(tablePuzzleList));
    # print(gameBoardPuzzleList);
    # print(tablePuzzleList);
    
    return getAnswer(gameBoardPuzzleList, tablePuzzleList);
