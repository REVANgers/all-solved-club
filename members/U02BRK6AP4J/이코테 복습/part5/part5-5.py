'''
음료수 얼려먹기
- n*m 크기의 얼음틀에서 0 그룹의 개수는?
- dfs 이용
- 현재 위치 기준 상하좌우를 살펴본 뒤, 해당 지점 값이 0이면 방문(True)
'''

n, m = map(int, input().split())
ans = 0
arr = []
for i in range(n):
    arr.append(list(input()))

def search(x, y):
    if not 0 <= x < n or not 0 <= y < m:
        return False
    if arr[x][y] == '0':
        arr[x][y] = '1'
        search(x - 1, y)
        search(x + 1, y)
        search(x, y - 1)
        search(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if search(i, j) == True:
            ans += 1
print(ans)