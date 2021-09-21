'''
성적이 낮은 순서로 학생 출력하기
- n의 개수만큼 이름과 성적을 받아서 성적이 낮은 순서대로 학생 이름 출력
'''
n = int(input())
d = []
for i in range(n):
    d.append(input().split())
d.sort(key=lambda x:x[1])
for i in d:
    print(i[0], end=' ')
