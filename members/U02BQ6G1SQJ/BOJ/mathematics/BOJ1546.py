import sys;

# sys.stdin = open("input1.txt", 'r');    # 75.0
# sys.stdin = open("input2.txt", 'r');    # 66.666667
# sys.stdin = open("input3.txt", 'r');    # 75.25
# sys.stdin = open("input4.txt", 'r');    # 38.75
# sys.stdin = open("input5.txt", 'r');    # 65.0
# sys.stdin = open("input6.txt", 'r');    # 32.5
# sys.stdin = open("input7.txt", 'r');    # 100.0
# sys.stdin = open("input8.txt", 'r');    # 55.55555555555556

N = int(sys.stdin.readline());
curScoreList = list(map(int, sys.stdin.readline().split()));
maxScore = max(curScoreList);
newScoreList = list(map(lambda k : (k * 100 / maxScore), curScoreList));

# print(N);
# print(curScoreList);
# print(newScoreList);
print(sum(newScoreList) / len(newScoreList));
