import collections;

class Solution:
    def minDeletions(self, s: str) -> int:
        answer = 0;
        sCounter = collections.Counter(s);
        frequencyCounter = collections.Counter([val for val in sCounter.values()]);
        
        # print(frequencyCounter);
        
        for key in sorted(frequencyCounter.keys(), key = lambda k : -k):
            # print("key :", key);
            # print("val :", frequencyCounter[key]);
            
            deleteCnt = 0;
            
            while (frequencyCounter[key] > 1) and (key > deleteCnt):
                deleteCnt += 1;
                
                if ((key - deleteCnt) not in frequencyCounter.keys()) or (frequencyCounter[key - deleteCnt] == 0):
                    (answer, frequencyCounter[key], frequencyCounter[key - deleteCnt]) = (answer + deleteCnt, frequencyCounter[key] - 1, frequencyCounter[key - deleteCnt] + 1);
                
                # print("deleteCnt :", deleteCnt);
                # print("answer :", answer);
                # print(frequencyCounter);
            
            if (frequencyCounter[key] > 1):
                (answer, frequencyCounter[key], frequencyCounter[0]) = (answer + (key * (frequencyCounter[key] - 1)), 1, frequencyCounter[0] + frequencyCounter[key] - 1);
            
            # print(frequencyCounter);
                    
        return answer;
