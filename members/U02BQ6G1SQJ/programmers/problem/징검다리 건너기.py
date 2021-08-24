(MIN_STONE, MAX_STONE) = (1, 200000000);

def checkPossible(stoneList : list, maxJump : int, candidateAnswer : int) -> bool:
    # print(stoneList);
    
    zeroCnt = 0;
    
    for curStone in stoneList:
        if (curStone > 0):
            zeroCnt = 0;
        else:
            zeroCnt += 1;
            
            if (zeroCnt == maxJump):
                return False;
    
    return True;

def solution(stones : list, k : int) -> int:
    (answer, left, right) = (0, MIN_STONE, MAX_STONE);
    
    while (left <= right):
        mid = (left + right) // 2;
        
        # print(mid, left, right);
        
        if (checkPossible(list(map(lambda k : k - mid, stones)), k, mid)):
            left = mid + 1;
        else:
            (answer, right) = (mid, mid - 1);
    
    return answer;
