# reference : https://velog.io/@seok1007/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%ED%81%B4%EB%A6%AC-%EC%B1%8C%EB%A6%B0%EC%A7%80-11%EC%A3%BC%EC%B0%A8-javascript

import collections;
import math;
# import itertools;

MAX_SIZE = 100;
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

"""
def addMinDict(minDict : collections.defaultdict, key : int, val : int) -> None:
    minDict[key] = min(minDict[key], val);
    return None;

def addMaxDict(maxDict : collections.defaultdict, key : int, val : int) -> None:
    maxDict[key] = max(maxDict[key], val);
    return None;
"""

def checkPos(startPos1 : int, endPos1 : int, startPos2 : int, endPos2 : int) -> bool:
    return (((startPos1 - endPos2) * (endPos1 - startPos2)) > 0);

def removePos(rectangleList : list, posSet : set, combinationTuple : tuple) -> None:
    (rectangleIdx1, rectangleIdx2) = combinationTuple;
    (startX1, startY1, endX1, endY1) = rectangleList[rectangleIdx1];
    (startX2, startY2, endX2, endY2) = rectangleList[rectangleIdx2];
    
    # print(rectangleIdx1, rectangleIdx2);
    # print(startX1, startY1, endX1, endY1);
    # print(startX2, startY2, endX2, endY2);
    # print();
    
    if ((checkPos(startX1, endX1, startX2, endX2)) or (checkPos(startY1, endY1, startY2, endY2))):
        return None;
        
    # print("XY");
    
    return None;

def checkImpossible(boardList : list, r : int, c : int) -> bool:
    return ((r < 0) or (r > MAX_SIZE) or (c < 0) or (c > MAX_SIZE) or (boardList[r][c] != 1))

def bfs(boardList : list, startR : int, startC : int, endR : int, endC : int) -> 0:
    dq = collections.deque([[startR, startC, 0]]);
    boardList[startR][startC] = math.inf;
    
    # print(startR, startC, endR, endC);
    
    while (dq):
        (curR, curC, curDist) = dq.popleft();
        
        # print(curR, curC, curDist);
        # print(dq);
        
        if ((curR, curC) == (endR, endC)):
            return (curDist // 2);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(boardList, nextR, nextC)):
                continue;
                
            boardList[nextR][nextC] = math.inf;
            dq.append([nextR, nextC, curDist + 1]);
        
    return -1;

def solution(rectangle : list, characterX : int, characterY : int, itemX : int, itemY : int) -> int:
    """
    (xMinDict, xMaxDict, yMinDict, yMaxDict) = (collections.defaultdict(lambda : math.inf), collections.defaultdict(lambda : 0), collections.defaultdict(lambda : math.inf), collections.defaultdict(lambda : 0));
    
    for (startX, startY, endX, endY) in rectangle:
        # print(startX, startY, endX, endY);
        
        for x in range(startX, endX + 1):
            # print("x :", x);
            
            addMinDict(xMinDict, x, startY);
            addMaxDict(xMaxDict, x, endY);
            
        for y in range(startY, endY + 1):
            # print("y :", y);
            
            addMinDict(yMinDict, y, startX);
            addMaxDict(yMaxDict, y, endX);
            
    print("xMinDict :", xMinDict);
    print("xMaxDict :", xMaxDict);
    print("yMinDict :", yMinDict);
    print("yMaxDict :", yMaxDict);
    """
    
    """
    posSet = set();
    
    for (startX, startY, endX, endY) in rectangle:
        # print(startX, startY, endX, endY);
        
        for x in range(startX, endX + 1):
            # print("x :", x);
            
            posSet.add(tuple([x, startY]));
            posSet.add(tuple([x, endY]));
            
        for y in range(startY, endY + 1):
            # print("y :", y);
            
            posSet.add(tuple([startX, y]));
            posSet.add(tuple([endX, y]));
            
    # print(sorted(posSet));
    
    for c in itertools.combinations([k for k in range(len(rectangle))], 2):
        # print(c);
        
        removePos(rectangle, posSet, c);
    """
    
    (boardList, rectangleList) = ([[0 for _ in range(MAX_SIZE + 1)] for _ in range(MAX_SIZE + 1)], [list(map(lambda k : k * 2, curRectangle)) for curRectangle in rectangle]);
    (characterC, characterR, itemC, itemR) = (map(lambda k : k * 2, [characterX, characterY, itemX, itemY]));
    
    for (startC, startR, endC, endR) in rectangleList:
        for r in range(startR, endR + 1):
            for c in range(startC, endC + 1):
                if ((r in [startR, endR]) or (c in [startC, endC])):
                    if (boardList[r][c] != 1):
                        boardList[r][c] += 1;
                else:
                    boardList[r][c] += 2;
                
    # print(boardList);
    # print(rectangleList);
    # print(characterC, characterR, itemC, itemR);
                
    return bfs(boardList, characterR, characterC, itemR, itemC);
