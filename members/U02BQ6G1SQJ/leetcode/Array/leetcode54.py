DIR_VEC = ((0, 1), (1, 0), (0, -1), (-1, 0));

def checkImpossible(matrixList : List[List[int]], isVisitedList : List[List[bool]], r : int, c : int) -> bool:
    return ((r < 0) or (r >= len(matrixList)) or (c < 0) or (c >= len(matrixList[r])) or (isVisitedList[r][c]));

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        (curR, curC, curDir) = (0, 0, 0);
        (answerList, isVisitedList) = ([], [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]);
        
        while (True):
            answerList.append(matrix[curR][curC]);
            isVisitedList[curR][curC] = True;
            (dr, dc) = DIR_VEC[curDir];
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if (checkImpossible(matrix, isVisitedList, nextR, nextC)):
                curDir = (curDir + 1) % len(DIR_VEC);
                (dr, dc) = DIR_VEC[curDir];
                (nextR, nextC) = (curR + dr, curC + dc);
                
            if (checkImpossible(matrix, isVisitedList, nextR, nextC)):
                break;
                
            (curR, curC) = (nextR, nextC);
            
        return answerList;
