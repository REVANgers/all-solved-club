'''
3. 퀵 정렬 -> 평균 O(nlog(n)) but 최악 O(n^2)
- 병합 정렬과 더불어 많이 사용되는 정렬 알고리즘
- 첫 번째 데이터를 피벗(pivot) 값으로 설정
- 피벗 값 기준으로 왼쪽부터 큰 값을 탐색, 오른쪽부터 작은 값을 탐색하여 swapping
- 만약 큰 값의 인덱스 > 작은 값의 인덱스(두 값이 엇갈릴 경우)에는 작은 값과 피벗 값을 swapping
    -> 피벗값 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽
- 재귀적으로 수행(왼쪽, 오른쪽 나누어서)
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(0)
    left = [i for i in arr if i <= pivot]
    right = [i for i in arr if i > pivot]
    return quick(left) + [pivot] + quick(right)
arr = quick(arr)
print(arr)
