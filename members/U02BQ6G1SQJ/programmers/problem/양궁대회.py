import collections;
import itertools;
import math;

MAX_SCORE = 10;

def solution(n : int, info : list) -> list:
    scoreDiff = -math.inf;
    answerList = [-1];
    infoList = list(reversed(info));
    apeachCounter = collections.Counter();

    for infoIdx in range(len(infoList)):
        apeachCounter[infoIdx] = infoList[infoIdx];

    # print(apeachCounter);
    # print(infoList);

    for cwr in itertools.combinations_with_replacement([k for k in range(MAX_SCORE + 1)], n):
        apeachScore = 0;
        ryanScore = 0;
        ryanCounter = collections.Counter(cwr);

        # print(cwr);
        # print(ryanCounter);

        for scoreIdx in apeachCounter.keys():
            if ((apeachCounter[scoreIdx] == 0) and (ryanCounter[scoreIdx] == 0)):
                continue;

            if (apeachCounter[scoreIdx] < ryanCounter[scoreIdx]):
                ryanScore += scoreIdx;
            else:
                apeachScore += scoreIdx;

        # print(apeachScore, ryanScore);

        if ((apeachScore < ryanScore) and (ryanScore - apeachScore > scoreDiff)):
            answerList.clear();

            for scoreIdx in range(MAX_SCORE + 1):
                answerList.append(ryanCounter[scoreIdx]);

            scoreDiff = ryanScore - apeachScore;

            # print(answerList);

        # print();

    return list(reversed(answerList));

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]));    # [0,2,2,0,1,0,0,0,0,0,0]
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]));    # [-1]
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]));    # [1,1,2,0,1,2,2,0,0,0,0]
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]));   # [1,1,1,1,1,1,1,1,0,0,2]
