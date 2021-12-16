import collections;

MAX_BIT_CNT = 8;

def getNextState(curState : Tuple[int]) -> Tuple[int]:
    return tuple([0] + ([1 if (curState[k - 1] == curState[k + 1]) else 0 for k in range(1, len(curState) - 1)]) + [0]);

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        (curDay, curState, adjDict, dayDict) = (0, tuple(cells), collections.defaultdict(tuple), collections.defaultdict(int));
        
        # print(curState);
        # print(len(adjList));
        
        while (curDay < n):
            if (curState in adjDict.keys()):
                dayDiff = (curDay - dayDict[curState]);
                curDay += (dayDiff * ((n - curDay) // dayDiff));
                break;
            else:
                (adjDict[curState], dayDict[curState]) = (getNextState(curState), curDay);
                (curDay, curState) = (curDay + 1, adjDict[curState]);
                
            # print(curDay, curState);
        
        # print(curDay);    
        # print(adjDict);
        # print(dayDict);
        
        while (curDay < n):
            (curDay, curState) = (curDay + 1, adjDict[curState]);
            
        return curState;
