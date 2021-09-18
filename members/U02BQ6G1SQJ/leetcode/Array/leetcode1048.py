import collections;
import string;

def checkPredecessor(wordA : str, wordB : str) -> bool:
    if (len(wordA) + 1 != len(wordB)):
        return False;
    
    (counterA, counterB) = (collections.Counter(wordA), collections.Counter(wordB));
    
    if ((len(counterA - counterB) != 0) or (len(counterB - counterA) != 1)):
        return False;
    
    for curCh in list(string.ascii_lowercase):
        for curIdx in range(len(wordB)):
            if ((wordA[ : curIdx] + curCh + wordA[curIdx : ]) == wordB):
                return True;
            
    return False;

def bfs(startWord : str, answerDict : dict, adjDict : dict) -> int:
    (maxChain, dq, visitSet) = (0, collections.deque([[startWord, 0]]), set([startWord]));
    
    while (dq):
        (curWord, curChain) = dq.popleft();
        maxChain = max(maxChain, curChain);
        
        if (curWord in answerDict.keys()):
            return (answerDict[curWord] + curChain);
        
        # print("curWord :", curWord, "curChain :", curChain, "maxChain :", maxChain);
        # print(adjDict[curWord]);
        
        for nextWord in adjDict[curWord]:
            # print("nextWord :", nextWord);
            
            if (nextWord in visitSet):
                continue;
                
            visitSet.add(nextWord);
            dq.append([nextWord, curChain + 1]);
            
    return maxChain;

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        (answerDict, adjDict) = (dict(), collections.defaultdict(list));
        
        for wordA in words:
            for wordB in words:
                if (checkPredecessor(wordA, wordB)):
                    adjDict[wordB].append(wordA);
                    
        # print(adjDict);
        
        for startWord in words:
            # print("startWord :", startWord);
            
            answerDict[startWord] = bfs(startWord, answerDict, adjDict);
            
        # print(answerDict);
            
        return (max(answerDict.values()) + 1);
