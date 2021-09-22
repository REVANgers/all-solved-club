'''
bisect_right(arr, n) : 해당 리스트에서 값이 n보다 큰 값의 첫 번째 인덱스 반환
bisect_left(arr, n) : 해당 리스트에서 값이 n보다 작거나 같은 값의 첫 번째 인덱스 반환
'''
from bisect import bisect_left, bisect_right
def count_by_range(a, left, right):
    right = bisect_right(a, right)
    left = bisect_left(a, left)
    return right - left

arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(arr, 4, 4)) # 값이 4인 데이터 개수 출력
print(count_by_range(arr, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력
