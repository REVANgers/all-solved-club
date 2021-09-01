import copy;

ROTATE_CNT = 4;

def rotateKey(keyList : list) -> list:
    return [list(reversed(k)) for k in list(zip(*keyList))];
    
def checkLock(lockList : list, lockStartR : int, lockStartC : int, lockEndR : int, lockEndC : int) -> bool:
    # for r in range(lockStartR, lockEndR):
    #     print(lockList[r][lockStartC : lockEndC]);
    
    for r in range(lockStartR, lockEndR):
        for c in range(lockStartC, lockEndC):
            if (lockList[r][c] != 1):
                return False;
    
    return True;
    
def checkPossible(keyList : list, lockList : list, keyLen : int, lockLen : int, diffR : int, diffC : int, lockStartR : int, lockStartC : int, lockEndR : int, lockEndC : int) -> bool:
    # print(lockStartR, lockStartC, lockEndR, lockEndC);
    # print(diffR, diffC);
    
    for r in range(keyLen):
        for c in range(keyLen):
            lockList[r + diffR][c + diffC] += keyList[r][c];
    
    isPossible = checkLock(lockList, lockStartR, lockStartC, lockEndR, lockEndC);
            
    for r in range(keyLen):
        for c in range(keyLen):
            lockList[r + diffR][c + diffC] -= keyList[r][c];
            
    return isPossible;
    
def solution(key : list, lock : list):
    (M, N) = (len(key), len(lock));
    newLock = [[0 for _ in range(2 * (M - 1) + N)] for _ in range(2 * (M - 1) + N)];
    
    for r in range(N):
        for c in range(N):
            newLock[r + M - 1][c + M - 1] = lock[r][c];
            
    # for r in range(2 * (M - 1) + N):
    #     print(newLock[r]);
    
    for r in range(M + N - 1):
        for c in range(M + N - 1):
            # print(r, c);
            
            newKey = copy.deepcopy(key);
            
            for rotateIdx in range(ROTATE_CNT):
                if (checkPossible(newKey, newLock, M, N, r, c, M - 1, M - 1, M + N - 1, M + N - 1)):
                    return True;
                
                newKey = rotateKey(newKey);
    
    return False;
