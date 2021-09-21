'''
정렬
- 데이터를 특정한 기준에 따라 순서대로 나열하는 것
1. 선택 정렬 -> O(n^2)
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 교환
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def minIdx(arr):
    x = 0
    for i in range(1, len(arr)):
        if arr[x] > arr[i]:
            x = i
    return x
def selection(arr):
    for i in range(len(arr) - 1):
        x = minIdx(arr[i:]) + i
        arr[i], arr[x] = arr[x], arr[i]
selection(arr)
print(arr)
