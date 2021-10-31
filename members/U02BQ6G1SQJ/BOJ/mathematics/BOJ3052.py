import sys;

(MOD, INPUT_CNT) = (42, 10);

# sys.stdin = open("input1.txt", 'r');    # 10
# sys.stdin = open("input2.txt", 'r');    # 1
# sys.stdin = open("input3.txt", 'r');    # 6

print(len(set(map(lambda k : (k % MOD), [int(sys.stdin.readline()) for _ in range(INPUT_CNT)]))));
