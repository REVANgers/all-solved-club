# 소요 시간 : 17분
import math;

def printMatrix(nodeCnt : int, matrix : list) -> None:
    for r in range(1, nodeCnt + 1):
        print(matrix[r]);
    
    return None;

def solution(n : int, s : int, a : int, b : int, fares : list) -> int:
    (answer, adjMatrix) = (math.inf, [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]);
    
    for (src, dst, fare) in fares:
        adjMatrix[src][dst] = fare;
        adjMatrix[dst][src] = fare;
    
    for passNode in range(1, n + 1):
        for startNode in range(1, n + 1):
            for endNode in range(1, n + 1):
                adjMatrix[startNode][endNode] = (0 if (startNode == endNode) else min(adjMatrix[startNode][endNode], adjMatrix[startNode][passNode] + adjMatrix[passNode][endNode]));
    
    # printMatrix(n, adjMatrix);
    
    for shareNode in range(1, n + 1):
        answer = min(answer, adjMatrix[s][shareNode] + adjMatrix[shareNode][a] + adjMatrix[shareNode][b]);
    
    return answer;
