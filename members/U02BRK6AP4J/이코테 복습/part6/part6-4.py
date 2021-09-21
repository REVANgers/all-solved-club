'''
4. 계수 정렬 -> O(n + k) 보장 (k: 데이터의 최대값)
- 데이터가 정수 형태일 때만 사용 가능
- bucket sort
- 데이터의 개수를 카운팅하여 정렬하는 기법
- 공간 복잡도가 큼
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
length = max(arr) + 1
bucket = [0] * length
for i in arr:
    bucket[i] += 1
for i in range(length):
    for j in range(bucket[i]):
        print(i)
