import collections;
import itertools;

def checkSquare(pointList : list, edgeList : list, permutationList : list) -> bool:
    edgeCounter = collections.Counter();
    
    for curIdx in range(len(permutationList) - 1):
        edgeCounter[edgeList[permutationList[curIdx]][permutationList[curIdx + 1]]] += 1;
        
    edgeCounter[edgeList[permutationList[3]][permutationList[0]]] += 1;
    
    # print(permutationList);
    # print(edgeCounter);
    
    return ((edgeCounter.most_common(1)[0][1] == len(edgeList)) and (edgeList[permutationList[0]][permutationList[2]] == edgeList[permutationList[1]][permutationList[3]]));

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pointList = [p1, p2, p3, p4];
        pointSet = set(map(tuple, pointList));
        
        if (len(pointList) > len(pointSet)):
            return False;
        
        edgeList = [[0 for _ in range(len(pointList))] for _ in range(len(pointList))];
    
        for i in range(len(pointList)):
            for j in range(i + 1, len(pointList)):
                (a, b) = pointList[i];
                (c, d) = pointList[j];
                edgeList[i][j] = ((a - c) ** 2 + (b - d) ** 2);
                edgeList[j][i] = edgeList[i][j];
        
        # print(edgeList);
        
        for p in itertools.permutations([k for k in range(len(pointList))], len(pointList)):
            if (checkSquare(pointList, edgeList, p)):
                return True;
            
        return False;
