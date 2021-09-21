'''
위에서 아래로
- 개수 n만큼의 숫자를 입력받아 내림차순
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in sorted(arr, reverse=True):
    print(i, end=' ')
