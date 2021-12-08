import collections;
import string;

(ALPHABET_CNT, ORD_DICT) = (len(string.ascii_lowercase), {k : ord(k) for k in string.ascii_lowercase});

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        strDict = collections.defaultdict(list);
        
        for curStr in strings:
            diffList = [];
            
            for chIdx in range(len(curStr) - 1):
                diffList.append((ORD_DICT[curStr[chIdx + 1]] - ORD_DICT[curStr[chIdx]] + ALPHABET_CNT) % ALPHABET_CNT);
                
            # print(curStr);
            # print(diffList);
            # print();
            
            strDict[tuple(diffList)].append(curStr);
            
        # print(strDict);
        
        return strDict.values();
