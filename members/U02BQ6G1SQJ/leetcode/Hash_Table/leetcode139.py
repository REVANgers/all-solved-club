import collections;

def bfs(wordStr : str, wordSet : set) -> bool:
    dq = collections.deque([0]);
    isVisitedList = [False for _ in range(len(wordStr) + 1)];
    isVisitedList[0] = True;
    
    while (dq):
        curIdx = dq.popleft();
        
        if (curIdx == len(wordStr)):
            return True;
        
        for nextIdx in range(curIdx + 1, len(wordStr) + 1):
            if ((isVisitedList[nextIdx]) or (wordStr[curIdx : nextIdx] not in wordSet)):
                continue;
            
            isVisitedList[nextIdx] = True;
            dq.append(nextIdx);
            
    return False;

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        (startIdx, wordSet) = (0, set(wordDict));
        
        for endIdx in range(1, len(s)):
            if (s[startIdx : endIdx] in wordSet):
                startIdx = endIdx;
                
        # print(startIdx);
                
        return s[startIdx : ] in wordSet;
        """
        
        wordSet = set(wordDict);
        return bfs(s, wordSet);
