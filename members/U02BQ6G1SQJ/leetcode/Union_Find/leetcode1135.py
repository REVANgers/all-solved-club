def find(parentDict : dict, curNode : int) -> int:
    if (parentDict[curNode] != curNode):
        parentDict[curNode] = find(parentDict, parentDict[curNode]);
        
    return parentDict[curNode];

def union(parentDict : dict, rankDict : dict, node1 : int, node2 : int) -> None:
    (root1, root2) = (find(parentDict, node1), find(parentDict, node2));
    
    if (rankDict[root1] < rankDict[root2]):
        parentDict[root1] = root2;
    else:
        parentDict[root2] = root1;
        
        if (rankDict[root1] == rankDict[root2]):
            rankDict[root1] += 1;
            
    return None;

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if (n > len(connections) + 1):
            return -1;
        
        (answer, parentDict, rankDict) = (0, dict(zip([k for k in range(1, n + 1)], [k for k in range(1, n + 1)])), dict(zip([k for k in range(1, n + 1)], [0 for k in range(1, n + 1)])));
        
        # print(parentDict);
        # print(rankDict);
        
        for (x, y, cost) in sorted(connections, key = lambda k : k[2]):
            # print(x, y, cost);
            
            if (find(parentDict, parentDict[x]) != find(parentDict, parentDict[y])):
                union(parentDict, rankDict, x, y);
                answer += cost;
                
        return answer;
