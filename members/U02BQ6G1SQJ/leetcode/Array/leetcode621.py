import collections;
import copy;

def bfs(taskCounter : collections.Counter, cooldownPeriod : int, startTask : str) -> int:
    taskCounter[startTask] -= 1;
    dq = collections.deque([[startTask, 1, taskCounter]]);
    
    while (dq):
        (curTaskStr, curTime, curCounter) = dq.popleft();
        
        if ((len(curCounter) == 0) or (curCounter.most_common(1)[0][1] == 0)):
            return curTime;
        
        for (key, val) in curCounter.items():
            if (val == 0):
                continue;
                
            if (len(curTaskStr) <= cooldownPeriod):
                if (key in curTaskStr):
                    continue;
            else:
                if (key in curTaskStr[len(curTaskStr) - cooldownPeriod : ]):
                    continue;
                    
            nextCounter = copy.deepcopy(curCounter);
            nextCounter[key] -= 1;
            dq.append([curTaskStr + key, curTime + 1, nextCounter]);
            
        dq.append([curTaskStr + "0", curTime + 1, copy.deepcopy(curCounter)]);
        
    return 0;

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        (answer, lastIdleCnt, taskCounter) = (0, 0, collections.Counter(tasks));
        
        # print(taskCounter.most_common(1)[0][0]);
        
        # return bfs(taskCounter, n, taskCounter.most_common(1)[0][0]);
        
        while (True):
            mostCommonList = taskCounter.most_common(n + 1);
            
            # print(mostCommonList);

            if (not mostCommonList):
                answer -= lastIdleCnt;
                break;
                
            for (key, val) in mostCommonList:
                taskCounter[key] -= 1;
                
                if (taskCounter[key] == 0):
                    del taskCounter[key];
                
            answer += (n + 1);
            
            if (len(mostCommonList) < n + 1):
                lastIdleCnt = n - len(mostCommonList) + 1;
            
        return answer;
