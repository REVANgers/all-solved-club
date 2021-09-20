'''
탐색
- BFS, DFS
- 자료구조(: 데이터를 표현하고 관리/처리하기 위한 구조) 사용
1. 스택
- 선입후출, 입구와 출구가 동일한 형태
- append, pop -> O(1)
2. 큐
- 선입선출, 입구와 출구가 모두 뚫려있는 형태
- collections 모듈의 deque()
- append, popleft / reverse
재귀 함수
- 자기 자신을 다시 호출하는 함수
- 코딩 테스트에서 사용 시에는 종료 조건 명시
- 스택 프레임 사용
'''
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)

print('for문으로 구현: ', fact(5))
print('재귀호출로 구현: ', fact_recur(5))
