'''
왕실의 나이트
- 8*8 평면(a~h + 1~8)에서 나이트의 움직일 수 있는 경우의 수는?
- 나이트는 수평/수직으로 두 칸 이동 + 수직/수평으로 한 칸 이동 가능
'''
import sys
pos = sys.stdin.readline()
x = ord(pos[0]) - 97
y = int(pos[1]) - 1
d = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]
arr = [[x + i[0], y + i[1]] for i in d]
ans = 0
for i in arr:
    if 0 <= i[0] < 8 and 0 <= i[1] < 8:
        ans += 1
print(ans)
