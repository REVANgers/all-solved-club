# import itertools;

def solution(n, left, right):
    """
    # 1. n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
    numList = [[0 for _ in range(n)] for _ in range(n)];

    # 2. i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
    for i in range(n):
        # print(i);

        # 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
        for r in range(i + 1):
            for c in range(i + 1):
                # print(r, c);

                if (numList[r][c] == 0):
                    numList[r][c] = i + 1;

    # print(numList2D);

    # 3. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
    # 4. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
    return list(itertools.chain.from_iterable(numList))[left : right + 1];
    """

    answerList = [];
    (curR, curC) = divmod(left, n);
    (endR, endC) = divmod(right, n);

    # print("end :", endR, endC);
    # print("cur :", curR, curC);

    while ((curR, curC) != (endR, endC)):
        answerList.append(max(curR, curC) + 1);

        if (curC == n - 1):
            (curR, curC) = (curR + 1, 0);
        else:
            curC += 1;

    answerList.append(max(curR, curC) + 1);
    return answerList;

# print(solution(3, 2, 5));   # [3,2,2,3]
# print(solution(4, 7, 14));  # [4,3,3,3,4,4,4,4]
