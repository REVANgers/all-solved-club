import sys;

DIGIT = 10;

# sys.stdin = open("input1.txt");

print(sum(list(map(lambda k : k ** 2, list(map(int, input().split()))))) % DIGIT);
