import sys;

(DIGIT, MAX_N, MOD) = (10, 100, 1000000000);
MAX_BIT = 1 << DIGIT;

# sys.stdin = open("input1.txt", "r");    # 1
# sys.stdin = open("input2.txt", "r");    # 3

N = int(sys.stdin.readline());

if (N < DIGIT):
    print(0);

    sys.exit(0);

dp = [[[0 for _ in range(MAX_BIT)] for _ in range(DIGIT)] for _ in range(N + 1)];

for c in range(DIGIT):
    dp[1][c][1 << c] = 1;

for r in range(2, N + 1):
    curBit = (1 << 0);

    for k in range(MAX_BIT):
        dp[r][0][k | curBit] = (dp[r][0][k | curBit] + dp[r - 1][1][k]) % MOD;

    for c in range(1, DIGIT - 1):
        curBit = (1 << c);

        for k in range(MAX_BIT):
            dp[r][c][k | curBit] = (dp[r][c][k | curBit] + dp[r - 1][c - 1][k] + dp[r - 1][c + 1][k]) % MOD;

    curBit = (1 << 9);

    for k in range(MAX_BIT):
        dp[r][9][k | curBit] = (dp[r][9][k | curBit] + dp[r - 1][8][k]) % MOD;

print(sum([dp[N][k][MAX_BIT - 1] for k in range(1, DIGIT)]) % MOD);
