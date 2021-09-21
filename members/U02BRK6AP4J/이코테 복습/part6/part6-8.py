'''
두 배열의 원소 교체
- k번만큼 b의 원소와 a의 원소를 swap해서 a의 최대 합 만들기
'''
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
print(sum(a[k:] + b[:k]))
