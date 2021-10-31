import sys;

MOD = 10;

SCORE_LIST = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A'];

# sys.stdin = open("input1.txt", 'r');

print(SCORE_LIST[int(sys.stdin.readline()) // MOD]);
