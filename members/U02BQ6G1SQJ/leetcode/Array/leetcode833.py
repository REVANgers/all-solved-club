def checkPossible(indiceIdx : int, indiceList : List[int], sourceList : List[str], replaceList : List[int]) -> bool:
    for chIdx in range(len(sourceList[indiceIdx])):
        if (replaceList[indiceList[indiceIdx] + chIdx] > 1):
            return False;
        
    return True;

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        (answerStr, sIdx, replaceList, isPossibleList, indiceDict, sourceDict, targetDict) = ("", 0, [0 for _ in range(len(s))], [True for _ in range(len(indices))], dict(), dict(), dict());
        
        for indiceIdx in range(len(indices)):
            (indiceDict[indices[indiceIdx]], sourceDict[indiceIdx], targetDict[indiceIdx]) = (indiceIdx, sources[indiceIdx], targets[indiceIdx]);
        
        # print(indiceDict);
        # print(sourceDict);
        # print(targetDict);
        
        for indiceIdx in range(len(indices)):
            if (s[indices[indiceIdx] : indices[indiceIdx] + len(sources[indiceIdx])] != sources[indiceIdx]):
                # print(s[indices[indiceIdx] : indices[indiceIdx] + len(sources[indiceIdx])], sources[indiceIdx]);
                
                isPossibleList[indiceIdx] = False;
                continue;
            
            for chIdx in range(len(sources[indiceIdx])):
                replaceList[indices[indiceIdx] + chIdx] += 1;
                
        # print(replaceList);
        
        for indiceIdx in range(len(indices)):
            if (not isPossibleList[indiceIdx]):
                continue;
            
            isPossibleList[indiceIdx] = checkPossible(indiceIdx, indices, sources, replaceList);
            
        # print(isPossibleList);
        
        for curIndice in sorted(indiceDict.keys()):
            indiceIdx = indiceDict[curIndice];
            
            # print(curIndice, indiceIdx);
            
            if (not isPossibleList[indiceIdx]):
                continue;
                
            (answerStr, sIdx) = (answerStr + s[sIdx : indices[indiceIdx]] + targets[indiceIdx], indices[indiceIdx] + len(sources[indiceIdx]));
            
            # print(sIdx);
            
        return (answerStr + s[sIdx : ]);
