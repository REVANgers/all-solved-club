import sys;

# sys.stdin = open("input1.txt", 'r');

print(*[k for k in range(1, int(sys.stdin.readline()) + 1)], sep = "\n");
