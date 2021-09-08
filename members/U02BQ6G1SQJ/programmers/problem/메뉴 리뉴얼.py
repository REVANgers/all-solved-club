# 소요 시간 : 21분
import collections;
import itertools;

MIN_ORDER_CNT = 2;

def solution(orders : list, course : list) -> list:
    (answerList, sortedOrderList) = ([], [sorted(list(k)) for k in orders]);
    
    # print(sortedOrderList);
    
    for courseCnt in course:
        courseDict = collections.defaultdict(int);
        
        for curOrder in sortedOrderList:
            for p in itertools.combinations(curOrder, courseCnt):
                # print(p);
                
                courseDict[p] += 1;

        if (not courseDict.values()):
            continue;
                
        maxOrderCnt = max(list(courseDict.values()));
        
        if (maxOrderCnt < MIN_ORDER_CNT):
            continue;
        
        for (key, val) in courseDict.items():
            if (val == maxOrderCnt):
                # print(key, val);
                
                answerList.append("".join(key));
        
        # print(courseDict);
        # print(maxOrderCnt);
    
    return sorted(answerList);
