import sys;

(ALPHABET_CNT, BIAS) = (26, ord("a"));

# sys.stdin = open("input1.txt", 'r');

answerList = [-1 for _ in range(ALPHABET_CNT)];

S = input();

# print(S);

for chIdx in range(len(S)):
    answerIdx = ord(S[chIdx]) - BIAS;

    if (answerList[answerIdx] == -1):
        answerList[answerIdx] = chIdx;

print(*answerList, sep = " ");
