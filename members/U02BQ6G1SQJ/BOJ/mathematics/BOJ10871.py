import sys;

# sys.stdin = open("input1.txt", 'r');

(N, X) = map(int, sys.stdin.readline().split());
A = list(map(int, sys.stdin.readline().split()));

# print(N, X);
# print(A);
print(*filter(lambda k : (k < X), A), sep = " ");
