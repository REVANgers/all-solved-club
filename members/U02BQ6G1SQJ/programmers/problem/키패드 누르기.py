import collections;
import math;

NUMBER_CNT = 12;
START_LEFT_HAND = 10;
START_MIDDLE_HAND = 11;
START_RIGHT_HAND = 12;
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));
KEYPAD_MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]];
ADJ_MATRIX = [[math.inf for _ in range(NUMBER_CNT + 1)] for _ in range(NUMBER_CNT + 1)];

def checkImpossible(r : int, c : int, dist : int, src : int) -> bool:
    return ((r < 0) or (r >= len(KEYPAD_MATRIX)) or (c < 0) or (c >= len(KEYPAD_MATRIX[r])) or (dist >= ADJ_MATRIX[src][KEYPAD_MATRIX[r][c]]));

def bfs(startR : int, startC : int) -> None:
    dq = collections.deque([[startR, startC, 0]]);
    startNum = KEYPAD_MATRIX[startR][startC];
    ADJ_MATRIX[startNum][startNum] = 0;
    
    while (dq):
        (curR, curC, curDist) = dq.popleft();
        curNum = KEYPAD_MATRIX[curR][curC];
        
        # print(curR, curC, curDist);
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC, nextDist) = (curR + dr, curC + dc, curDist + 1);

            if (checkImpossible(nextR, nextC, nextDist, startNum)):
                continue;
                
            nextNum = KEYPAD_MATRIX[nextR][nextC];
            ADJ_MATRIX[startNum][nextNum] = nextDist;
            dq.append([nextR, nextC, nextDist]);
            
            # print(nextR, nextC, nextDist, nextNum);
        
    return None;

def solution(numbers : list, hand : str) -> str:
    (answer, leftHand, rightHand) = ('', START_LEFT_HAND, START_RIGHT_HAND);
    
    for r in range(len(KEYPAD_MATRIX)):
        for c in range(len(KEYPAD_MATRIX[r])):
            bfs(r, c);
    
    # print(ADJ_MATRIX);
    
    for curNum in list(map(lambda k : (START_MIDDLE_HAND if (k == 0) else k), numbers)):
        (leftDist, rightDist) = (ADJ_MATRIX[curNum][leftHand], ADJ_MATRIX[curNum][rightHand]);
        
        if (curNum % 3 == 1):
            (answer, leftHand) = (answer + "L", curNum);
            continue;
        elif (curNum % 3 == 0):
            (answer, rightHand) = (answer + "R", curNum);
            continue;
            
        # print(curNum);
        # print(leftHand, rightHand);
        # print(leftDist, rightDist);
        # print();
        
        if (leftDist < rightDist):
            (answer, leftHand) = (answer + "L", curNum);
            continue;
        elif (leftDist > rightDist):
            (answer, rightHand) = (answer + "R", curNum);
            continue;
        
        if (hand == "left"):
            (answer, leftHand) = (answer + "L", curNum);
        elif (hand == "right"):
            (answer, rightHand) = (answer + "R", curNum);
    
    return answer;
