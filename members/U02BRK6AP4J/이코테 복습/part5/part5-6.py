'''
미로 탈출
- n*m 크기의 직사각형 형태의 미로가 주어짐
- 내 위치는 (1, 1)이고 미로의 출구는 (n,m)
- 괴물이 없는 부분인 1을 따라 미로를 탈출해야 함
- bfs를 사용하여 이동한 노드 값 +1씩
'''
from collections import deque
n, m = map(int, input().split())
d = [
    [-1, 0], [1, 0], [0, -1], [0, 1]
]
arr = []
for i in range(n):
    arr.append(list(input()))

def search(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in d:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '1':
                arr[nx][ny] += arr[x][y]
                queue.append([nx, ny])
    return arr[n - 1][m - 1]
ans = len(search(0, 0))
print(ans)
