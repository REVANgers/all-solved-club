import sys;

sys.setrecursionlimit(1000000);
MAX_DIR = 5;

# sys.stdin = open("input1.txt", 'r');

def move(src : int, dst : int) -> int:
    if (src == 0):
        return 2;
    elif (src == dst):
        return 1;
    elif ((src % 2) == (dst % 2)):
        return 4;

    return 3;

def solve(cmdIdx : int, leftPos : int, rightPos : int, cmdList : list, dp : list) -> int:
    if (cmdIdx == len(cmdList) - 1):
        return 0;

    if (dp[cmdIdx][leftPos][rightPos] != 0):
        return dp[cmdIdx][leftPos][rightPos];

    dp[cmdIdx][leftPos][rightPos] = min(solve(cmdIdx + 1, cmdList[cmdIdx], rightPos, cmdList, dp) + move(leftPos, cmdList[cmdIdx]), solve(cmdIdx + 1, leftPos, cmdList[cmdIdx], cmdList, dp) + move(rightPos, cmdList[cmdIdx]));
    return dp[cmdIdx][leftPos][rightPos];

cmdList = list(map(int, sys.stdin.readline().split()));

# print(cmdList);

dp = [[[0 for _ in range(MAX_DIR)] for _ in range(MAX_DIR)] for _ in range(len(cmdList))];

print(solve(0, 0, 0, cmdList, dp));
