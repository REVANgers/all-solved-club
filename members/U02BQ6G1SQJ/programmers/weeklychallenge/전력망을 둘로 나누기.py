import collections;
import math;

def bfs(nodeCnt : int, startNode : int, adjList : list) -> int:
    visitCnt = 0;
    dq = collections.deque([startNode]);
    isVisitedList = [False for _ in range(nodeCnt + 1)];
    isVisitedList[startNode] = True;
    
    # print("startNode :", startNode);
    # print(adjList);
    
    while (dq):
        curNode = dq.popleft();
        visitCnt += 1;
        
        # print("curNode :", curNode);
        
        for nextNode in adjList[curNode]:
            if (isVisitedList[nextNode]):
                continue;
                
            isVisitedList[nextNode] = True;
            dq.append(nextNode);
        
    # print("visitCnt :", visitCnt);
        
    return visitCnt;

def solution(n : int, wires : list):
    (answer, adjList) = (math.inf, [set() for _ in range(n + 1)]);
    
    for (src, dst) in wires:
        adjList[src].add(dst);
        adjList[dst].add(src);
        
    # print(adjList);
    
    for (src, dst) in wires:
        isVisitedList = [False for _ in range(n + 1)];
        
        adjList[src].remove(dst);
        adjList[dst].remove(src);
        
        answer = min(answer, abs(n - (bfs(n, src, adjList) * 2)));
        
        # print("src :", src);
        # print("dst :", dst);
        # print(adjList);
        # print("answer :", answer);
        # print();
        
        adjList[src].add(dst);
        adjList[dst].add(src);
    
    return answer;
