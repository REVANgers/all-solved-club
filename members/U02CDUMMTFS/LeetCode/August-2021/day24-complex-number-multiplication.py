# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3917/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1.replace('i', '').split('+'))
        real2, imag2 = map(int, num2.replace('i', '').split('+'))
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        answer = f"{real}+{imag}i"
        return answer
