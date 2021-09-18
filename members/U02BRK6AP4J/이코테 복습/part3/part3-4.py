'''
1이 될 때까지
- n, k가 주어질 때, n이 1이 될 때까지의 최소 횟수
- 아래 경우 중 하나 선택 가능
- n -= 1
- n /= k
-> 해설: n은 무조건 1이 될 수 있음(양의 정수이므로)
    k로 나누는 것이 무조건 이득
'''
import sys
n, k = map(int, sys.stdin.readline().split())
ans = 0
''' 이렇게 짜면 나중에 n이 커질 때 비효율적
while n > 1:
    if n % k == 0: n /= k
    else: n -= n % k
    ans += n % k
print(ans)
'''
while True:
    if n % k == 0:
        ans += 1
        n /= k
    else:
        ans += n % k
        n -= n % k
    if n < k: break
print(ans + n - 1)