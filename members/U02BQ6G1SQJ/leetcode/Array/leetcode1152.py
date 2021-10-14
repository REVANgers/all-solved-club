import collections;
import itertools;

PATTERN_SIZE = 3;

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        (maxKey, maxVal, patternCounter, patternDict) = ([], 0, collections.Counter(), collections.defaultdict(list));
        
        for usernameIdx in range(len(username)):
            patternDict[username[usernameIdx]].append([timestamp[usernameIdx], website[usernameIdx]]);
            
        # print(patternDict);
        
        for val in patternDict.values():
            (timestampList, websiteList) = zip(*sorted(val, key = lambda k : k[0]));
            
            # print(timestampList);
            # print(websiteList);
            # print();
            
            if (len(websiteList) < PATTERN_SIZE):
                continue;
            
            for c in set(combinations(websiteList, PATTERN_SIZE)):
                patternCounter[c] += 1;
                
        # print(patternCounter);
        
        for (key, val) in patternCounter.items():
            if (maxVal < val) or ((maxVal == val) and (maxKey > key)):
                (maxKey, maxVal) = (key, val);
                
        return maxKey;
