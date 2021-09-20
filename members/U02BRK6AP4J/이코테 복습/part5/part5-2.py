'''
유클리드 호제법(gcd 구하기)
- A와 B의 최대공약수 == B와 A%B의 최대공약수
- math 모듈의 gcd
'''
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))
