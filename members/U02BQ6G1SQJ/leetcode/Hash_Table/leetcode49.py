import collections;

(ALPHABET_CNT, BIAS) = (26, ord("a"));

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = collections.defaultdict(list);
        
        for curStr in strs:
            cntList = [0 for _ in range(ALPHABET_CNT)];
            
            for curCh in curStr:
                cntList[ord(curCh) - BIAS] += 1;
                
            anagramDict[tuple(cntList)].append(curStr);
            
        # print(anagramDict);
        
        return [k for k in anagramDict.values()];
