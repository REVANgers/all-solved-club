import collections;
import itertools;

def mergeSet(nameDict : collections.defaultdict(list), curName : str, combinationTuple : tuple) -> bool:
    (setIdx1, setIdx2) = combinationTuple;
    
    if ((not nameDict[curName][setIdx1]) or (not nameDict[curName][setIdx2])):
        return False;
    
    if (nameDict[curName][setIdx1] & nameDict[curName][setIdx2]):
        nameDict[curName][setIdx1] |= nameDict[curName][setIdx2];
        nameDict[curName][setIdx2].clear();
        return True;
        
    return False;

def mergeAccount(nameDict : collections.defaultdict(list), curName : str):
    for c in itertools.combinations([k for k in range(len(nameDict[curName]))], 2):
        if (mergeSet(nameDict, curName, c)):
            return True;
        
    return False;

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        (answerList, nameDict) = ([], collections.defaultdict(list));
        
        for accountList in accounts:
            curName = accountList[0];
            nameDict[curName].append(set(accountList[1 : ]));
                
        for curName in nameDict.keys():
            while (mergeAccount(nameDict, curName)):
                continue;
                
        for curName in nameDict.keys():
            for accountSet in nameDict[curName]:
                if (not accountSet):
                    continue;
                
                answerList.append([curName] + sorted(list(accountSet)));
            
        return answerList;
