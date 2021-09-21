'''
2. 삽입 정렬 -> O(n^2) but 최선의 경우에는 O(n)
- 앞 쪽 데이터를 정렬이 된 데이터라고 간주하고 뒤 쪽 데이터를 순서대로 뽑아 앞 쪽 데이터의 적절한 위치에 삽입
    -> 두 번째 데이터부터 정렬 수행
- 선택 정렬보다 효율적이지만 까다로움
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

insertion(arr)
print(arr)
