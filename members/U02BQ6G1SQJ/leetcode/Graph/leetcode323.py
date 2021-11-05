import collections;

def bfs(startNode : int, adjList : List[List[int]], isVisitedList : List[bool]) -> int:
    dq = collections.deque([startNode]);
    
    while (dq):
        curNode = dq.popleft();
        
        for nextNode in adjList[curNode]:
            if (isVisitedList[nextNode]):
                continue;
                
            isVisitedList[nextNode] = True;
            dq.append(nextNode);
        
    return 1;

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        (answer, adjList, isVisitedList) = (0, [[] for _ in range(n)], [False for _ in range(n)]);
        
        for (src, dst) in edges:
            adjList[src].append(dst);
            adjList[dst].append(src);
            
        # print(adjList);
        
        for curNode in range(n):
            if (isVisitedList[curNode]):
                continue;
                
            isVisitedList[curNode] = True;
            answer += bfs(curNode, adjList, isVisitedList);
            
        return answer;
