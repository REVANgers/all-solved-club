# 소요 시간 : 106분
import collections;
import itertools;
import math;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(boardList : list, r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(boardList)) or (c < 0) or (c >= len(boardList[r])));

def getCtrlPos(boardList : list, startR : int, startC : int, dr : int, dc : int) -> list:
    (curR, curC) = (startR + dr, startC + dc);
    
    while (not checkImpossible(boardList, curR, curC)):
        if (boardList[curR][curC] != 0):
            return (curR, curC);
        
        (curR, curC) = (curR + dr, curC + dc);
        
    return [curR - dr, curC - dc];    

def pushQueue(dq : collections.deque, isVisitedList : list, r : int, c : int, cnt : int) -> None:
    if (isVisitedList[r][c]):
        return None;
    
    isVisitedList[r][c] = True;
    dq.append([r, c, cnt]);
    return None;

def setBoardList(boardList : list, cardDict : dict, boardStatus : int) -> None:
    for curCard in cardDict.keys():
        # print(curCard, boardStatus, (boardStatus & 1 << (curCard - 1)) >> (curCard - 1));
        
        boardValue = curCard;
        
        if ((boardStatus & 1 << (curCard - 1)) >> (curCard - 1)):
            boardValue = 0;
            
        for (curR, curC) in cardDict[curCard]:
            boardList[curR][curC] = boardValue;
            
    # print(boardStatus);
    # print(boardList);
    
    return None;

def bfs(boardList : list, cardDict : dict, boardStatus : int, startR : int, startC : int, endR : int, endC : int) -> int:
    dq = collections.deque([[startR, startC, 0]]);
    isVisitedList = [[False for _ in range(len(boardList[0]))] for _ in range(len(boardList))];
    
    setBoardList(boardList, cardDict, boardStatus);
    
    # print([startR, startC], [endR, endC]);
    
    while (dq):
        (curR, curC, curCnt) = dq.popleft();
        
        # print(curR, curC, curCnt);
        
        if ((curR, curC) == (endR, endC)):
            # print(curCnt);
            
            return (curCnt + 1);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(boardList, nextR, nextC)):
                continue;
                
            (ctrlR, ctrlC) = getCtrlPos(boardList, curR, curC, dr, dc);
            pushQueue(dq, isVisitedList, nextR, nextC, curCnt + 1);
            pushQueue(dq, isVisitedList, ctrlR, ctrlC, curCnt + 1);
    
    return 0;

def getFindPairCnt(boardList : list, cardDict : dict, boardStatus : int, startR : int, startC : int, passR : int, passC : int, endR : int, endC : int) -> int:
    return (bfs(boardList, cardDict, boardStatus, startR, startC, passR, passC) + bfs(boardList, cardDict, boardStatus, passR, passC, endR, endC));

def backtrack(boardList : list, cardDict : dict, boardStatus : int, startR : int, startC : int, permutationTuple : tuple, depth : int) -> int:
    if (depth == len(permutationTuple)):
        return 0;
    
    (curCard, findPairCnt) = (permutationTuple[depth], 0);
    (r1, c1) = cardDict[curCard][0];
    (r2, c2) = cardDict[curCard][1];
    # 초기 위치 -> 첫 번째 카드 위치 -> 두 번째 카드 위치
    findPairCnt1 = getFindPairCnt(boardList, cardDict, boardStatus, startR, startC, r1, c1, r2, c2);
    # 초기 위치 -> 두 번째 카드 위치 -> 첫 번째 카드 위치
    findPairCnt2 = getFindPairCnt(boardList, cardDict, boardStatus, startR, startC, r2, c2, r1, c1);
    boardStatus ^= (1 << (curCard - 1));
    
    # print("boardStatus :", boardStatus, "findPairCnt :", findPairCnt);
    
    if (findPairCnt1 < findPairCnt2):
        return (findPairCnt1 + backtrack(boardList, cardDict, boardStatus, r2, c2, permutationTuple, depth + 1));
    elif (findPairCnt1 > findPairCnt2):
        return (findPairCnt2 + backtrack(boardList, cardDict, boardStatus, r1, c1, permutationTuple, depth + 1));
    
    return min((findPairCnt1 + backtrack(boardList, cardDict, boardStatus, r2, c2, permutationTuple, depth + 1)), (findPairCnt2 + backtrack(boardList, cardDict, boardStatus, r1, c1, permutationTuple, depth + 1)));

def solution(board : list, r : int, c : int) -> int:
    answer = math.inf;
    
    # cardSet = set(itertools.chain.from_iterable(board));
    # cardSet.remove(0);
    # print(cardSet);
    
    cardDict = collections.defaultdict(list);
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 0):
                continue;
                
            cardDict[board[row][col]].append([row, col]);
            
    # print(cardDict); 
            
    for p in itertools.permutations(cardDict.keys(), len(cardDict)):
        (boardStatus, findAllCnt, curR, curC) = (0, 0, r, c);
        
        setBoardList(board, cardDict, boardStatus);
        findAllCnt = backtrack(board, cardDict, boardStatus, r, c, p, 0);
                
        # print(p, answer, findAllCnt);
                
        answer = min(answer, findAllCnt);
    
    return answer;
