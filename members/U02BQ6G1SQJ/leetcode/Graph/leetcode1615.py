import itertools;

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        (answer, adjList) = (0, [set() for _ in range(n)]);
        
        for roadIdx in range(len(roads)):
            (src, dst) = roads[roadIdx];
            adjList[src].add(tuple([src, dst, roadIdx]));
            adjList[dst].add(tuple([src, dst, roadIdx]));
            
        # print(adjList);
        
        for (city1, city2) in itertools.combinations([k for k in range(n)], 2):
            # print(city1, city2);
            
            answer = max(answer, len(adjList[city1] | adjList[city2]));
            
        return answer;
