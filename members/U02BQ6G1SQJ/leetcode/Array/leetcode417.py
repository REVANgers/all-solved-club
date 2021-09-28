import collections;

# (PACIFIC_DIR_VEC, ATLANTIC_DIR_VEC) = (((-1, 0), (0, -1)), ((1, 0), (0, 1)));
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

"""
def checkPacificPossible(heightList: List[List[int]], r : int, c : int) -> int:
    if ((r < 0) or (c < 0) or (r > len(heightList) - 1) or (c > len(heightList[r]) - 1)):
        return -1;
    elif ((r == 0) or (c == 0)):
        return 0;
    
    return 1;

def checkAtlanticPossible(heightList: List[List[int]], r : int, c : int) -> int:
    if ((r < 0) or (c < 0) or (r > len(heightList) - 1) or (c > len(heightList[r]) - 1)):
        return -1;
    elif ((r == len(heightList) - 1) or (c == len(heightList[r]) - 1)):
        return 0;
    
    return 1;

def bfs(heightList: List[List[int]], possibleList : List[List[bool]], checkPossible : Callable, startR : int, startC : int) -> None:
    dq = collections.deque([[startR, startC]]);
    isVisitedList = [[False for _ in range(len(heightList[0]))] for _ in range(len(heightList))];
    isVisitedList[startR][startC] = True;
    
    # print("start :", startR, startC);
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        # print("cur :", curR, curC);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            # print("next :", nextR, nextC);
        
            checkResult = checkPossible(heightList, nextR, nextC);
            
            # print("checkResult :", checkResult);
            
            if (checkResult == -1):
                # print("checkResult == -1");
                
                continue;
            
            if (isVisitedList[nextR][nextC]):
                # print("isVisitedList[nextR][nextC]");
                
                continue;
                
            isVisitedList[nextR][nextC] = True;
            
            if (heightList[curR][curC] < heightList[nextR][nextC]):
                # print("heightList[curR][curC] < heightList[nextR][nextC]");
                
                continue;
                
            if ((checkResult == 0) or (possibleList[nextR][nextC])):
                # print("(checkResult == 0) or (possibleList[nextR][nextC])");
                
                (possibleList[startR][startC], possibleList[curR][curC], possibleList[nextR][nextC]) = (True, True, True);
                return None;
                
            # print("append");
            
            dq.append([nextR, nextC]);
        
    return None;
"""

def bfs(heightList : List[List[int]], visitedList : List[List[bool]], startR : int, startC : int) -> None:
    if (visitedList[startR][startC]):
        return None;
    
    dq = collections.deque([[startR, startC]]);
    visitedList[startR][startC] = True;
    
    # print(startR, startC);
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if ((nextR < 0) or (nextR >= len(heightList)) or (nextC < 0) or (nextC >= len(heightList[nextR])) or (visitedList[nextR][nextC]) or (heightList[curR][curC] > heightList[nextR][nextC])):
                continue;
                
            visitedList[nextR][nextC] = True;
            dq.append([nextR, nextC]);
    
    # print(visitedList);
            
    return None;

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        (answerList, pacificPossibleList, atlanticPossibleList) = ([], [[False for _ in range(len(heights[0]))] for _ in range(len(heights))], [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]);
                    
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (checkPacificPossible(heights, r, c) == 0):
                    pacificPossibleList[r][c] = True;
                    continue;
                
                if (not pacificPossibleList[r][c]):
                    bfs(heights, pacificPossibleList, checkPacificPossible, r, c);
                    
                # print(r, c);
                # print(pacificPossibleList);
                # print();
                    
        for r in reversed(range(len(heights))):
            for c in reversed(range(len(heights[r]))):
                if (checkAtlanticPossible(heights, r, c) == 0):
                    atlanticPossibleList[r][c] = True;
                    continue;
                
                if (not atlanticPossibleList[r][c]):
                    bfs(heights, atlanticPossibleList, checkAtlanticPossible, r, c);
                    
                # print(r, c);
                # print(atlanticPossibleList);
                # print();
        
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if ((pacificPossibleList[r][c]) and (atlanticPossibleList[r][c])):
                    answerList.append([r, c]);
                    
        return answerList;
        """
        
        (answerList, pacificVisitedList, atlanticVisitedList) = ([], [[False for _ in range(len(heights[0]))] for _ in range(len(heights))], [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]);
            
        (pacificVisitedList[0][0], atlanticVisitedList[len(heights) - 1][len(heights[len(heights) - 1]) - 1]) = (True, True);
            
        for r in range(1, len(heights)):
            bfs(heights, pacificVisitedList, r, 0);
            
        for c in range(1, len(heights[0])):
            bfs(heights, pacificVisitedList, 0, c);
            
        # print(pacificVisitedList);
            
        for r in range(0, len(heights) - 1):
            bfs(heights, atlanticVisitedList, r, len(heights[r]) - 1);
            
        for c in range(0, len(heights[len(heights) - 1]) - 1):
            bfs(heights, atlanticVisitedList, len(heights) - 1, c);
            
        # print(atlanticVisitedList);
            
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (pacificVisitedList[r][c]) and (atlanticVisitedList[r][c]):
                    answerList.append([r, c]);
                    
        return answerList;
