def checkRowImpossible(startR : int, startC : int, rowSet : set, colSet : set) -> bool:
    return ((startR != 0) and (tuple([startR - 1, startC]) not in rowSet) and (tuple([startR, startC - 1]) not in colSet) and (tuple([startR, startC]) not in colSet));

def checkColImpossible(startR : int, startC : int, rowSet : set, colSet : set) -> bool:
    return ((tuple([startR - 1, startC]) not in rowSet) and (tuple([startR - 1, startC + 1]) not in rowSet) and ((tuple([startR, startC - 1]) not in colSet) or (tuple([startR, startC + 1]) not in colSet)));
    
def uninstallRow(startR : int, startC : int, rowSet : set, colSet : set) -> None:
    rowSet.remove(tuple([startR, startC]));
    
    if ((tuple([startR + 1, startC]) in rowSet) and (checkRowImpossible(startR + 1, startC, rowSet, colSet))):
        rowSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR, startC - 1]) in colSet) and (checkColImpossible(startR, startC - 1, rowSet, colSet))):
        rowSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR, startC]) in colSet) and (checkColImpossible(startR, startC, rowSet, colSet))):
        rowSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR + 1, startC - 1]) in colSet) and (checkColImpossible(startR + 1, startC - 1, rowSet, colSet))):
        rowSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR + 1, startC]) in colSet) and (checkColImpossible(startR + 1, startC, rowSet, colSet))):
        rowSet.add(tuple([startR, startC]));
        return None;
    
    return None;

def uninstallCol(startR : int, startC : int, rowSet : set, colSet : set) -> None:
    colSet.remove(tuple([startR, startC]));
    
    if ((tuple([startR, startC]) in rowSet) and (checkRowImpossible(startR, startC, rowSet, colSet))):
        colSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR, startC + 1]) in rowSet) and (checkRowImpossible(startR, startC + 1, rowSet, colSet))):
        colSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR, startC - 1]) in colSet) and (checkColImpossible(startR, startC - 1, rowSet, colSet))):
        colSet.add(tuple([startR, startC]));
        return None;
    
    if ((tuple([startR, startC + 1]) in colSet) and (checkColImpossible(startR, startC + 1, rowSet, colSet))):
        colSet.add(tuple([startR, startC]));
        return None;
    
    return None;

def installRow(startR : int, startC : int, rowSet : set, colSet : set) -> None:
    if (checkRowImpossible(startR, startC, rowSet, colSet)):
        return None;
    
    rowSet.add(tuple([startR, startC]));
    return None;

def installCol(startR : int, startC : int, rowSet : set, colSet : set) -> None:
    if (checkColImpossible(startR, startC, rowSet, colSet)):
        return None;
    
    colSet.add(tuple([startR, startC]));
    return None;

def solution(n : int, build_frame : list) -> list:
    (rowSet, colSet) = (set(), set());
    
    for (c, r, structure, command) in build_frame:
        # print(r, c, command, structure);
        
        if (command == 0):
            # 기둥 삭제
            if (structure == 0):
                uninstallRow(r, c, rowSet, colSet);
            # 보 삭제
            elif (structure == 1):
                uninstallCol(r, c, rowSet, colSet);
        elif (command == 1):
            # 기둥 설치
            if (structure == 0):
                installRow(r, c, rowSet, colSet);
            # 보 설치
            elif (structure == 1):
                installCol(r, c, rowSet, colSet);
                
    # print(rowSet);
    # print(colSet);
    # print();
    
    return sorted([[curRow[1], curRow[0], 0] for curRow in rowSet] + [[curCol[1], curCol[0], 1] for curCol in colSet], key = lambda k : (k[0], k[1], k[2]));
