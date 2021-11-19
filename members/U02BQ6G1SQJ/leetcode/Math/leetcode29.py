MIN_INT = -2147483648;

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return ((-MIN_INT - 1) if ((dividend == MIN_INT) and (divisor == -1)) else int(dividend / divisor));
