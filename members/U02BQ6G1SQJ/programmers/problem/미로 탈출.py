# 소요 시간 : 65분
# 카카오 공식 문제 풀이를 먼저 확인한 후, 해설 내용에 맞게 코드를 구현했습니다. 
# 문제 풀이 reference : https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/
import collections;
import heapq;
import math;

def checkReversed(trapDict : dict, curState : int, curNode : int) -> bool:
    if (curNode not in trapDict.keys()):
        return False;
    
    return (((1 << trapDict[curNode]) & curState) >> trapDict[curNode]);

def getNextState(trapDict : dict, curState : int, nextNode : int) -> int:
    if (nextNode not in trapDict.keys()):
        return curState;
    
    return ((1 << trapDict[nextNode]) ^ curState);

def pushNextNode(pq : list, trapDict : dict, visitList : list, curState : int, nextTime : int, nextNode : int) -> None: 
    if (visitList[nextNode][curState] <= nextTime):
        return None;

    visitList[nextNode][curState] = nextTime;
    nextState = getNextState(trapDict, curState, nextNode);
    heapq.heappush(pq, [nextTime, nextState, nextNode]);
    
    # print("nextTime :", nextTime, "nextState :", nextState, "nextNode :", nextNode);
    
    return None;

def bfs(nodeCnt : int, startNode : int, endNode : int, trapList : list, outdegreeDict : dict, indegreeDict : dict) -> int:
    pq = [[0, 0, startNode]];
    trapDict = dict(zip([key for key in trapList], [val for val in range(len(trapList))]));
    # 또한, 원래의 다익스트라 알고리즘에서는 한 번 방문한 노드는 다시 방문할 필요가 없으나, 이 문제에서는 입출력 예 #2에서처럼 한 번 방문한 노드를 다시 방문해야 하는 경우도 있습니다. 
    # 이 경우는 방문할 때마다 그래프의 상태가 달랐기 때문으로, 다익스트라 알고리즘에서 “이미 방문한 정점”을 확인할 때 그래프의 상태가 달라진 경우에는 제외해서는 안 됩니다.
    visitList = [[math.inf for _ in range(2 ** len(trapList))] for _ in range(nodeCnt + 1)];
    
    # print(trapDict);
    # print(visitList);
    
    # TRAP이 있는 경우는 어떻게 해야 할까요? 
    # 문제의 조건에서, TRAP 노드의 최대 개수는 10입니다. 
    # 즉, TRAP 노드의 수가 적기 때문에 다익스트라 알고리즘을 사용하면서 그래프의 상태(즉, 어떤 노드에 연결된 간선들이 뒤집어져 있는지)까지 고려할 수 있습니다. 
    while (pq):
        (curTime, curState, curNode) = heapq.heappop(pq);
        
        # print("curTime :", curTime, "curState :", curState, "curNode :", curNode);
        
        if (curNode == endNode):
            return curTime;
        
        curReversed = checkReversed(trapDict, curState, curNode);
        
        # print("outdegree");
        
        # 다익스트라 알고리즘에서 특정 노드를 방문하고, 다음 방문할 노드를 우선순위 큐에 넣는 과정에서 그래프의 상태를 확인하여 그 노드로 들어오는 간선과 노드에서 나가는 간선 중 사용 가능한 간선만을 골라서 사용하게 되는 것입니다. 
        for nextNode in outdegreeDict[curNode]:
            nextReversed = checkReversed(trapDict, curState, nextNode);
            
            # print(curReversed, nextReversed, nextNode);
            
            if (curReversed ^ nextReversed):
                continue;
                
            nextTime = curTime + outdegreeDict[curNode][nextNode]; 
            pushNextNode(pq, trapDict, visitList, curState, nextTime, nextNode);
        
        # print("indegree");
        
        # 일반적인 다익스트라 알고리즘 구현에서는 노드에서 나가는 간선만 고려하면 되지만, 이 문제에서는 들어오는 간선도 TRAP으로 인해 나가는 간선으로 바뀔 수 있기 때문에 모두 확인해 주어야 합니다. 
        for nextNode in indegreeDict[curNode]:
            # print(curReversed, nextReversed, nextNode);
            
            nextReversed = checkReversed(trapDict, curState, nextNode);
            
            if (not (curReversed ^ nextReversed)):
                continue;

            nextTime = curTime + indegreeDict[curNode][nextNode];
            pushNextNode(pq, trapDict, visitList, curState, nextTime, nextNode);
    
    return -1;

def solution(n : int, start : int, end : int, roads : list, traps : list) -> int:
    outdegreeDict = [collections.defaultdict(lambda : math.inf) for _ in range(n + 1)];
    indegreeDict = [collections.defaultdict(lambda : math.inf) for _ in range(n + 1)];
    
    for (src, dst, time) in roads:
        outdegreeDict[src][dst] = min(outdegreeDict[src][dst], time);
        indegreeDict[dst][src] = min(outdegreeDict[src][dst], time);
        
    # print(outdegreeDict);
    # print(indegreeDict);
    
    return bfs(n, start, end, traps, outdegreeDict, indegreeDict);
