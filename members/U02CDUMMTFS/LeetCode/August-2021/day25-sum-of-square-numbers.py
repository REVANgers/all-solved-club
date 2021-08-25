class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root_c = int(c ** 0.5)
        for i in range(root_c + 1):
            a = i ** 2
            b = c - a
            root_b = b ** 0.5
            if root_b == int(root_b):
                return True
        return False
