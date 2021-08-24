import re;
import collections;

def solution(s : str) -> list:
    (answer, resultCounter) = ([], collections.Counter());
    tupleList = list(filter(lambda k : k not in ["", ","], sorted(re.split("{|}", s), key = lambda k : len(k))));
    
    # print(tupleList);
    
    for curTuple in tupleList:
        tupleCounter = collections.Counter(curTuple.split(","));
        answer.append(int((tupleCounter - resultCounter).most_common(1)[0][0]));
        resultCounter = tupleCounter;
        
        # print(tupleCounter - resultCounter);
    
    return answer;
