import math;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));
LEFT_VEC = (2, 3, 1, 0);
RIGHT_VEC = (3, 2, 0, 1);


def checkCycle(gridList : list, visitList : list, rowCnt : int, colCnt : int, startRow : int, startCol : int, startDir : int) -> int:
    (cycleLen, r, c, d) = (0, startRow, startCol, startDir);

    while (True):
        # 전진
        (dr, dc) = DIR_VEC[d];
        (r, c) = ((r + dr) % rowCnt, (c + dc) % colCnt);
        
        # 방향 전환
        if (gridList[r][c] == "L"):
            d = LEFT_VEC[d];
        elif (gridList[r][c] == "R"):
            d = RIGHT_VEC[d];

        cycleLen += 1;

        if ((r, c, d) == (startRow, startCol, startDir)):
            break;

        visitList[r][c][d] = cycleLen;

    return cycleLen;


def solution(grid: list) -> list:
    (rowCnt, colCnt) = (len(grid), len(grid[0]));
    (answerList, visitList) = ([], [[[math.inf for _ in range(len(DIR_VEC))] for _ in range(colCnt)] for _ in range(rowCnt)]);

    for r in range(rowCnt):
        for c in range(colCnt):
            for d in range(len(DIR_VEC)):
                if (visitList[r][c][d] != math.inf):
                    continue;

                visitList[r][c][d] = 0;
                cycleLen = checkCycle(grid, visitList, rowCnt, colCnt, r, c, d);

                if (cycleLen != 0):
                    answerList.append(cycleLen);

    return sorted(answerList);

# print(solution(["SL","LR"]));   # [16]
# print(solution(["S"]));         # [1,1,1,1]
# print(solution(["R","R"]));     # [4,4]
