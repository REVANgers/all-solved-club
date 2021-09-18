'''
게임 개발
- n*m 크기의 직사각형 맵 존재
- 캐릭터는 동서남북 중 하나의 방향을 가짐(0: 북, 1: 동, 2: 남, 3: 서)
- 각 칸은 육지 또는 바다로 이루어짐
'''
import sys
n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
maps = []
ans = 1
dArr = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
maps[x][y] = 2
while True:
    if maps[x - 1][y] >= 1 and maps[x + 1][y] >= 1 and maps[x][y - 1] >= 1 and maps[x][y + 1] >= 1:
        if maps[x - dArr[d][0]][y - dArr[d][1]] == 0:
            x -= dArr[d][0]
            y -= dArr[d][1]
            maps[x][y] = 2
            ans += 1
        else:
            break
    else:
        d = (d - 1) % 4
        if maps[x + dArr[d][0]][y + dArr[d][1]] == 0:
            x += dArr[d][0]
            y += dArr[d][1]
            maps[x][y] = 2
            ans += 1
print(ans)
