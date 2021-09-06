# 소요 시간 : 24분
STRAIGHT_DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));
DIAGONAL_DIR_VEC = ((-1, -1), (-1, 1), (1, -1), (1, 1));

def checkImpossiblePos(placeList : list, r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(placeList)) or (c < 0) or (c >= len(placeList[r])));

def checkImpossibleCase1(placeList : list, curR : int, curC : int) -> bool:
    for (dr, dc) in STRAIGHT_DIR_VEC:
        (nextR, nextC) = (curR + dr, curC + dc);
        
        if (checkImpossiblePos(placeList, nextR, nextC)):
            continue;
            
        if (placeList[nextR][nextC] == "P"):
            return True;
    
    return False;   

def checkImpossibleCase2(placeList : list, curR : int, curC : int) -> bool:
    for (dr, dc) in STRAIGHT_DIR_VEC:
        (nextR, nextC) = (curR + (dr * 2), curC + (dc * 2));
        
        if (checkImpossiblePos(placeList, nextR, nextC)):
            continue;
            
        (midR, midC) = (curR + dr, curC + dc);
        
        if ((placeList[nextR][nextC] == "P") and (placeList[midR][midC] != "X")):
            return True;
    
    return False;

def checkImpossibleCase3(placeList : list, curR : int, curC : int) -> bool:
    for (dr, dc) in DIAGONAL_DIR_VEC:
        (nextR, nextC) = (curR + dr, curC + dc);
        
        if (checkImpossiblePos(placeList, nextR, nextC)):
            continue;
            
        (midR1, midC1, midR2, midC2) = (curR, nextC, nextR, curC);
        
        if ((placeList[nextR][nextC] == "P") and ((placeList[midR1][midC1] != "X") or (placeList[midR2][midC2] != "X"))):
            return True;
    
    return False;

def checkImpossible(placeList : list, r : int, c : int) -> bool:
    # 1. 인접한 경우, 즉 맨해튼 거리가 1인 경우
    if (checkImpossibleCase1(placeList, r, c)):
        return True;
    
    # 2. 직선으로 맨해튼 거리가 2인 경우
    if (checkImpossibleCase2(placeList, r, c)):
        return True;
    
    # 3. 대각선으로 맨해튼 거리가 2인 경우
    if (checkImpossibleCase3(placeList, r, c)):
        return True;
    
    return False;

def getAnswer(placeList : list) -> bool:
    for r in range(len(placeList)):
        for c in range(len(placeList[r])):
            if ((placeList[r][c] == "P") and (checkImpossible(placeList, r, c))):
                return False;
    
    return True;

def solution(places : list) -> int:
    answerList = [];
    
    for placeList in places:
        answerList.append(int(getAnswer(placeList)));
    
    return answerList;
