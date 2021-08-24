import itertools;

def checkID(userID : str, userIdx : int, bannedID : str, bannedIdx : int, memoList : list) -> None:
    if (len(userID) != len(bannedID)):
        memoList[userIdx][bannedIdx] = 0;
        return;
    
    for chIdx in range(len(userID)):
        if ((bannedID[chIdx] != "*") and (userID[chIdx] != bannedID[chIdx])):
            memoList[userIdx][bannedIdx] = 0;
            return;
    
    memoList[userIdx][bannedIdx] = 1;
    return;

def checkPermutation(userIDList : str, bannedIDList : str, memoList : str, permutation : tuple) -> bool:
    for bannedIdx in range(len(bannedIDList)):
        userIdx = permutation[bannedIdx];

        if (memoList[userIdx][bannedIdx] == -1):
            # print(userIdx, bannedIdx);

            checkID(userIDList[userIdx], userIdx, bannedIDList[bannedIdx], bannedIdx, memoList);

        if (memoList[userIdx][bannedIdx] == 0):
            return False;
        
    return True;

def solution(user_id : str, banned_id : str) -> int:
    (answerSet, memoList) = (set(), [[-1 for _ in range(len(banned_id))] for _ in range(len(user_id))]);
    
    for curP in itertools.permutations([k for k in range(len(user_id))], len(banned_id)):
        if (checkPermutation(user_id, banned_id, memoList, curP)):
            answerSet.add(tuple(sorted(curP)));
    
    # print(answerSet);
    # print(memoList);
    
    return len(answerSet);
