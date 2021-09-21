'''
파이썬 정렬 라이브러리
- sort(), sorted()
- 병합 정렬 기반 => 최악의 경우에도 O(nlong) 보장
'''
arr = [('당근', 3), ('바나나', 2), ('사과', 5)]
arr.sort(key=lambda x:x[1])
print(arr)