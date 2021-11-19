import collections;

def bfs(startR : int, startC : int, adjDict : collections.defaultdict, visitSet : set) -> int:
    dq = collections.deque([[startR, startC]]);
    
    while (dq):
        (curR, curC) = dq.popleft();
        
        for (nextR, nextC) in adjDict[tuple([curR, curC])]:
            # print(nextR, nextC);
            
            if (tuple([nextR, nextC]) in visitSet):
                continue;
                
            visitSet.add(tuple([nextR, nextC]));
            dq.append([nextR, nextC]);
    
    return 1;

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        (answer, adjDict, visitSet) = (0, collections.defaultdict(set), set());
        
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                (srcR, srcC) = stones[i];
                (dstR, dstC) = stones[j];
                
                # print(srcR, srcC, dstR, dstC);
                
                if ((srcR == dstR) or (srcC == dstC)):
                    adjDict[tuple([srcR, srcC])].add(tuple([dstR, dstC]));
                    adjDict[tuple([dstR, dstC])].add(tuple([srcR, srcC]));
                    
        # print(adjDict);
        
        for (r, c) in stones:
            # print(r, c);
            
            posTuple = tuple([r, c]);
            
            if (posTuple in visitSet):
                continue;
                
            visitSet.add(posTuple);
            answer += bfs(r, c, adjDict, visitSet);
            
        return (len(stones) - answer);
