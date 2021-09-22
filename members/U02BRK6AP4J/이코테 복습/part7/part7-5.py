'''
정렬된 배열에서 특정 수의 개수 구하기
- n개의 원소를 갖는 오름차순 배열에서 x가 등장하는 횟수 계산
- 시간 복잡도 O(logn)
'''
'''
def search(arr, start, end, n):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            ans = mid
            break
    return ans
print(search(arr, 0, n - 1, x + 1) - search(arr, 0, n - 1, x - 1) - 1)
'''
from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
arr = list(map(int, input().split()))
def search(arr, n):
    ans = bisect_right(arr, n, n) - bisect_left(arr, n, n)
    return ans == 0 and -1 or ans
print(search(arr, x))
