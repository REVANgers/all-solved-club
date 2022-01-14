import math;

def convertNotation(srcNum : int, dstNotation : int) -> str:
    dstStr = "";

    while (srcNum > 0):
        (srcNum, dstDigit) = divmod(srcNum, dstNotation);
        dstStr = str(dstDigit) + dstStr;

    return dstStr;


def checkPrime(num: int) -> int:
    if (num == 1):
        return -1;

    """
    # for divisor in range(2, math.ceil(math.sqrt(num))):
    for divisor in range(2, num):
        if (num % divisor == 0):
            return -1;
    """

    divisor = 2;

    while (divisor ** 2 <= num):
        if (num % divisor == 0):
            return -1;

        divisor += 1;

    return num;

def solution(n : int, k : int) -> int:
    answer = 0;
    primeSet = set();
    pList = convertNotation(n, k).split("0");

    # print(pList);
    # print(convertNotation(1000000, 2));
    # print(len(convertNotation(1000000, 2)));

    for curP in pList:
        # print(checkPrime(int(curP)));

        if (not curP):
            continue;

        if (curP in primeSet):
            answer += 1;
            continue;

        primeResult = checkPrime(int(curP));

        if (primeResult != -1):
            primeSet.add(primeResult);
            answer += 1;

    # print(primeSet);

    return answer;

# print(solution(437674, 3));  # 3
# print(solution(110011, 10)); # 2
# print(solution(1, 10)); # 0
# print(solution(1, 2)); # 0
