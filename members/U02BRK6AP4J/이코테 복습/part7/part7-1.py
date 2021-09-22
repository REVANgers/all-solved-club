'''
순차 탐색 vs 이진 탐색
- 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색
- 시작점, 끝점, 중간점을 이용하여 탐색 범위 설정
- 이진 탐색의 시간 복잡도: O(logn)
'''
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
n = 15  # 찾고자 하는 수
'''
def binary(arr, start, end, n):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            return mid
    return -1
'''
def binary(arr, start, end, n):
    mid = (start + end) // 2
    if start > end:
        return -1
    if arr[mid] < n:
        return binary(arr, mid + 1, end, n)
    elif arr[mid] > n:
        return binary(arr, start, mid - 1, n)
    else:
        return mid

idx = binary(arr, 0, len(arr) - 1, n)
print(idx)
