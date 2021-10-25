# import heapq;
import itertools;

def exploreDungeons(k : int, dungeonList : list, permutationList : list) -> int:
    (exploreCnt, curFatigue) = (0, k);
    
    for dungeonIdx in permutationList:
        (minimumRequiredFatigue, exhaustionFatigue) = dungeonList[dungeonIdx];
        
        if (curFatigue < minimumRequiredFatigue):
            break;
            
        (exploreCnt, curFatigue) = (exploreCnt + 1, curFatigue - exhaustionFatigue);
        
    return exploreCnt;

def solution(k : int, dungeons : list) -> int:
    """
    (answer, curFatigue, pq) = (0, k, [[-curDungeon[0], curDungeon[1]] for curDungeon in dungeons]);
    heapq.heapify(pq);
    
    # print(pq);
    
    while (pq):
        (minimumRequiredFatigue, exhaustionFatigue) = heapq.heappop(pq);
        
        if (curFatigue >= minimumRequiredFatigue):
            (answer, curFatigue) = (answer + 1, curFatigue - exhaustionFatigue);
            
    return answer;
    """
    
    answer = 0;
    
    for p in itertools.permutations([dungeonIdx for dungeonIdx in range(len(dungeons))], len(dungeons)):
        # print(p);
        
        answer = max(answer, exploreDungeons(k, dungeons, p));
    
    return answer;
