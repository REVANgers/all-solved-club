n = int(input())
arr = []
for i in range(n):
    arr.append([i] + list(map(int, input().split())))
arr = sorted(arr, reverse=True, key=lambda x:(x[1], x[2]))

ans = [0] * n
rank = 1

t = arr[0]
ans[t[0]] = rank
for i in range(1, n):
    t = arr[i]
    rank = len([j for j in range(i) if arr[j][1] > t[1] and arr[j][2] > t[2]]) + 1
    ans[t[0]] = rank
for i in ans:
    print(i, end=' ')