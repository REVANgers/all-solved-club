import itertools;

def addList(answerList : list, src : int, dst : int) -> None:
    answerList[src].add(dst);
    answerList[dst].add(src);
    return None;

def checkMeet(answerList : list, src : int, dst : int, enterList : list, leaveList : list, enterOrderList : list, leaveOrderList : list) -> None:
    if (enterOrderList[src] > enterOrderList[dst]):
        (src, dst) = (dst, src);

    if (set(enterList[enterOrderList[dst] + 1 : ]) & set(leaveList[ : leaveOrderList[src]])):
        addList(answerList, src, dst);
    
    return None;

def solution(enter : list, leave : list) -> list:
    """
    answerList = [set() for _ in range(len(enter) + 1)];
    leaveList = [-1 for _ in range(len(leave) + 1)];
        
    for leaveIdx in range(len(leave)):
        leaveList[leave[leaveIdx]] = leaveIdx;   
    
    roomSet = set();
    leaveIdx = 0;

    for curEnter in enter:
        tmpIdx = leaveList[curEnter];
        roomSet.add(curEnter);
        
        # print("enterIdx :", enterIdx);
        # print("leaveIdx :", leaveIdx);
        # print("tmpIdx :", tmpIdx);
        # print("curEnter :", curEnter);
        # print("roomSet :", roomSet);
        
        for (src, dst) in itertools.combinations(roomSet, 2):
            # print(src, dst);
            
            answerList[src].add(dst);
            answerList[dst].add(src);
        
        while (leaveIdx < len(leave)):
            curLeave = leave[leaveIdx];

            if (curLeave not in roomSet):
                break;

            roomSet.remove(curLeave);
            leaveIdx += 1;
            
        # print();
        
    # print(answerList);
    
    return [len(k) for k in answerList[1 : ]];
    """
    
    answerList = [set() for _ in range(len(enter) + 1)];
    (enterOrderList, leaveOrderList) = ([-1 for _ in range(len(enter) + 1)], [-1 for _ in range(len(leave) + 1)]);
    
    for enterIdx in range(len(enter)):
        enterOrderList[enter[enterIdx]] = enterIdx;
        
    for leaveIdx in range(len(leave)):
        leaveOrderList[leave[leaveIdx]] = leaveIdx;
    
    for (person1, person2) in itertools.combinations(enter, 2):
        # print(person1, person2);
        # print(enterOrderList[person1], enterOrderList[person2], leaveOrderList[person1], leaveOrderList[person2]);
        
        if ((enterOrderList[person1] < enterOrderList[person2]) ^ (leaveOrderList[person1] < leaveOrderList[person2])):
            addList(answerList, person1, person2);
        else:
            checkMeet(answerList, person1, person2, enter, leave, enterOrderList, leaveOrderList);
            
    # print(answerList);
    # print(enterList);
    # print(leaveList);
    
    return [len(k) for k in answerList[1 : ]];
