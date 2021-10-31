import sys;

# sys.stdin = open("input1.txt", 'r');    # 437
# sys.stdin = open("input2.txt", 'r');    # 132
# sys.stdin = open("input3.txt", 'r');    # 938

print(max(map(int, map(''.join, map(reversed, sys.stdin.readline().split())))));
