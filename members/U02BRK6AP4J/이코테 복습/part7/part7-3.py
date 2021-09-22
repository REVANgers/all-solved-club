'''
트리 자료구조
- 그래프 자료구조의 일종
- 노드와 노드의 연결로 표현됨
- DBMS나 파일 시스템에서 데이터 관리에 주로 사용
- 루트 노드, 단말 나도, 서브 트리 등

이진 탐색 트리
- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

부품 찾기
- 부품의 개수 n 입력 -> 부품 리스트 입력
    -> 찾는 부품 개수 m 입력 -> 찾는 부품 리스트 입력
    -> 부품이 있으면 yes, 없으면 no 출력
'''
n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
arr2 = sorted(map(int, input().split()))
ans = []
def search(arr, start, end, n):
    ans = 'no'
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            ans = 'yes'
            break
    return ans
for i in arr2:
    print(search(arr, 0, n - 1, i), end=' ')
