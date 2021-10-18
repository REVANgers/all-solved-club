MOD = 1;

def solution(n):
    for x in range(1, n):
        if (n % x == MOD):
            return x;

    return 0;

# print(solution(10));    # 2
# print(solution(12));    # 11
