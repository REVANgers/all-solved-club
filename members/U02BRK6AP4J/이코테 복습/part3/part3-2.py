'''
큰 수의 법칙(하)
- 다양한 수 n개를 갖는 배열이 있을 때, 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙
- k번을 초과하여 더할 수 없음
'''
import sys
n, m, k = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()), reverse=True)
tmp = m // k
ans = arr[0] * (m - tmp) + arr[1] * tmp
print(ans)
