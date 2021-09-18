DIGIT = 10;

def solution(numbers : list) -> int:
    return sum(set([k for k in range(DIGIT)]) - set(numbers));

# print(solution([1,2,3,4,6,7,8,0])); # 14
# print(solution([5,8,4,0,6,7,9]));   # 6
