'''
곱하기 혹은 더하기
- 숫자(0~9)로 이루어진 문자열 숫자 사이에 x 혹은 + 연산자를 넣어 가장 큰 수 만들기
'''
s = input()
ans = int(s[0])
for i in range(1, len(s)):
    if int(s[i - 1]) <= 1 or int(s[i]) <= 1:
        ans += int(s[i])
    else:
        ans *= int(s[i])
print(ans)
