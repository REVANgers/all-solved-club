import itertools;

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        (answer, setList) = (0, list(map(set, filter(lambda k : len(set(k)) == len(k), arr))));
        
        # print(setList);
        
        if (not setList):
            return 0;
        
        for strCnt in range(1, len(setList) + 1):
            for c in itertools.combinations(setList, strCnt):
                # print(c);
                
                (lenSum, lenUnion) = (sum([len(k) for k in c]), len(c[0].union(*c[1 : ])));
                
                if (lenSum == lenUnion):
                    answer = max(answer, lenSum);
                    
        return answer;
