'''
모험가 길드
- n명의 모험가는 공포도 x를 가짐
- 공포도 x인 모험가는 반드시 x명 이상 그룹에 참여해야 함
- 구성할 수 있는 최대 그룹 수? (모든 모험가를 데리고 가지 않아도 됨)
'''
import sys
n = int(sys.stdin.readline())
ans = 0
arr = sorted(map(int, sys.stdin.readline().split()))
m = max(arr)  # 최대값
i = 1  # 시작값
while True:
    ans += arr.count(i) // i
    i += 1
    if i == m:
        break
print(ans)
