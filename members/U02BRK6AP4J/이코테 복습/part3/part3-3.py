'''
숫자 카드 게임(하)
- 각 행마다의 최소값 중에 최대값 구하기
'''
import sys
n, m = map(int, sys.stdin.readline().split())
ans = 0
for i in range(n):
    ans = max(ans, sorted(map(int, sys.stdin.readline().split()))[0])
print(ans)
