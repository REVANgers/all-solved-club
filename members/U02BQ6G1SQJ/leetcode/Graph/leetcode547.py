import collections;

def bfs(isConnected : List[List[int]], isVisitedList : List[bool], startNode : int) -> int:
    dq = collections.deque([startNode]);
    
    while (dq):
        curNode = dq.popleft();
        
        for nextNode in range(len(isConnected[curNode])):
            if ((isVisitedList[nextNode]) or (isConnected[curNode][nextNode] == 0)):
                continue;
                
            isVisitedList[nextNode] = True;
            dq.append(nextNode);
            
    return 1;

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        (answer, isVisitedList) = (0, [False for _ in range(len(isConnected))]);
        
        for startNode in range(len(isConnected)):
            if (isVisitedList[startNode]):
                continue;
                
            answer += bfs(isConnected, isVisitedList, startNode);
            
        return answer;
