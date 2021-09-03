import math;
import itertools;

def getNextWeakIdx(curWeakIdx : int, curDist : int, weakList : list) -> int:
    for nextWeakIdx in range(curWeakIdx + 1, len(weakList)):
        if (weakList[nextWeakIdx] - weakList[curWeakIdx] > curDist):
            return nextWeakIdx;
        
    return len(weakList);

def getAnswer(answer : int, weakList : list, distList : list) -> int:
    (weakIdx, distIdx) = (0, 0);
    
    while ((weakIdx < len(weakList)) and (distIdx < len(distList))):
        if (weakIdx == len(weakList) - 1):
            (weakIdx, distIdx) = (weakIdx + 1, distIdx + 1);
            break;
            
        weakIdx = getNextWeakIdx(weakIdx, distList[distIdx], weakList);
        distIdx += 1;
        
        if (distIdx == answer):
            break;
        
    return (distIdx if (weakIdx == len(weakList)) else (distIdx + 1));

def solution(n : int, weak : list, dist : list) -> int:
    (answer, circleWeakList) = (math.inf, weak + list(map(lambda k : (k + n), weak)));
    
    # print(circleWeakList);
        
    for startIdx in range(len(weak)):
        # print(circleWeakList[startIdx : startIdx + len(weak)]);
        
        for p in itertools.permutations(dist, len(dist)):
            answer = min(answer, getAnswer(answer, circleWeakList[startIdx : startIdx + len(weak)], p));
            
            # print(circleWeakList[startIdx : startIdx + len(weak)], p, answer);
    
    return (-1 if (answer > len(dist)) else answer);
