import collections;

def bfs(startNode : int, timeList : list, adjList : list) -> int:
    (maxTime, dq) = (0, collections.deque([[startNode, 0]]));
    
    while (dq):
        (curNode, curTime) = dq.popleft();
        maxTime = max(maxTime, curTime);
        
        for nextNode in adjList[curNode]:
            dq.append([nextNode, curTime + timeList[curNode]]);
            
    return maxTime;

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = [[] for _ in range(n)];
        
        for childNode in range(n):
            # print(manager[childNode], childNode);
            
            if (manager[childNode] != -1):
                adjList[manager[childNode]].append(childNode);
            
        # print(adjList);
        
        return bfs(headID, informTime, adjList);
