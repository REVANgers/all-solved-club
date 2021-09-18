'''
문자열 재정렬
- 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력이 주어지면 알파벳은 오름차순, 숫자는 합 값을 구하여 이어서 출력
'''
arr = sorted(input())
ans = 0
while True:
    tmp = arr.pop(0)
    if ord(tmp) < 65:
        ans += int(tmp)
    else:
        ans = tmp + ''.join(arr) + str(ans)
        break
print(ans)
