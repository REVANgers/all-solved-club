import sys;

MINUTE_DIFF = 45;

# sys.stdin = open("input1.txt", 'r');    # 9 25
# sys.stdin = open("input2.txt", 'r');    # 23 45
# sys.stdin = open("input3.txt", 'r');    # 22 55

(H, M) = map(int, sys.stdin.readline().split());
M -= MINUTE_DIFF;

if (M < 0):
    (H, M) = ((H + 23) % 24, M + 60);

print(H, M);
