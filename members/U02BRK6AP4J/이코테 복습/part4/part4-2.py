'''
시각
- 정수 n이 입력되면, 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구해야 함
- 완전 탐색 문제(brute force)
'''
import sys
n = int(sys.stdin.readline())
# 3, 13, 23시일 경우 = 3600
# 위 시가 아닌 경우 = 15 * 60 + 45 * 15 = 1575
ans = 0
while n:
    if n % 3 == 0:
        ans += 3600
    else:
        ans += 1575
    n -= 1
print(ans + 1575)
