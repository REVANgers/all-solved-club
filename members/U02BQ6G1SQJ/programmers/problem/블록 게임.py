# 시험 당시 작성한 코드 : 없음

# 부스트캠프 이후 작성 코드
import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkBoardImpossible(boardList : list, boardVisitList : list, r : int, c : int, squareValue : int) -> bool:
    return ((r < 0) or (r >= len(boardList)) or (c < 0) or (c >= len(boardList[r]) or (boardList[r][c] != squareValue) or (boardVisitList[r][c])));

def getBlockDiff(a : list, b : list) -> list:
    return [b[0] - a[0], b[1] - a[1]];

def getEmptyList(squareList : list) -> list:
    blockDiffList = [getBlockDiff(squareList[0], squareList[k]) for k in range(len(squareList))];
    (startR, startC) = squareList[0];
    
    # print("blockDiffList :", blockDiffList);
    
    if (blockDiffList[1] == [1, 0]):
        if (blockDiffList[2] == [1, 1]):
            if (blockDiffList[3] == [1, 2]):
                return [[startR, startC + 1], [startR, startC + 2]];
        elif (blockDiffList[2] == [2, -1]):
            return [[startR, startC - 1], [startR + 1, startC - 1]];
        elif (blockDiffList[2] == [2, 0]):
            return [[startR, startC + 1], [startR + 1, startC + 1]];
    elif (blockDiffList[1] == [1, -2]):
        return [[startR, startC - 2], [startR, startC - 1]];
    elif (blockDiffList[1] == [1, -1]):
        if (blockDiffList[3] == [1, 1]):
            return [[startR, startC - 1], [startR, startC + 1]];
        
    return [];

def bfs(boardList : list, blockList : list, emptyList : list, boardVisitList : list, startR : int, startC : int) -> None:
    (nonZeroSquareList, dq) = ([], collections.deque([[startR, startC]]));
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        nonZeroSquareList.append([curR, curC]);
            
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkBoardImpossible(boardList, boardVisitList, nextR, nextC, boardList[curR][curC])):
                continue;
                
            boardVisitList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
    
    nonZeroSquareList.sort(key = lambda k : (k[0], k[1]));
    zeroSquareList = getEmptyList(nonZeroSquareList);
    
    # print("nonZeroSquareList :", nonZeroSquareList);
    # print("zeroSquareList :", zeroSquareList);
    
    if (zeroSquareList != []):
        blockList.append(nonZeroSquareList);
        emptyList.append(zeroSquareList);
        
    return None;

def getLastRow(boardList : list, c : int) -> int:
    for r in range(len(boardList)):
        if (boardList[r][c] > 0):
            return (r - 1);
            
    return (len(boardList) - 1);

def checkBlockImpossible(zeroSquareList : list, lastRowList : list) -> int:
    for (emptyR, emptyC) in zeroSquareList:
        # print(emptyR, emptyC);

        if ((emptyR != lastRowList[emptyC] - 1) and (emptyR != lastRowList[emptyC])):
            return True;
    
    return False;

def checkBoardPossible(boardList : list, blockList : list, emptyList : list, blockVisitList : list, lastRowList : list) -> bool:
    for blockIdx in range(len(blockVisitList)):
        if ((blockVisitList[blockIdx]) or (checkBlockImpossible(emptyList[blockIdx], lastRowList))):
            continue;

        blockVisitList[blockIdx] = True;
        changedColSet = set([k[1] for k in blockList[blockIdx]]);

        # print(changedColSet);

        for (blockR, blockC) in blockList[blockIdx]:
            boardList[blockR][blockC] = 0;

        for changedC in changedColSet:
            lastRowList[changedC] = getLastRow(boardList, changedC);

        return True;

    # print(blockVisitList);
    # print(lastRowList);
    
    return False;

def solution(board : list) -> int:
    (answer, blockList, emptyList) = (0, [], []);
    boardVisitList = [[False for _ in range(len(board[0]))] for _ in range(len(board))];
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if ((board[r][c] == 0) or (boardVisitList[r][c])):
                continue;
                
            boardVisitList[r][c] = True;
            bfs(board, blockList, emptyList, boardVisitList, r, c);
            
    # print("blockList :", blockList);
    # print("emptyList :", emptyList);
    
    blockVisitList = [False for _ in range(len(blockList))];
    lastRowList = [getLastRow(board, c) for c in range(len(board[0]))];
    
    while (checkBoardPossible(board, blockList, emptyList, blockVisitList, lastRowList)):
        answer += 1;
    
    return answer;
