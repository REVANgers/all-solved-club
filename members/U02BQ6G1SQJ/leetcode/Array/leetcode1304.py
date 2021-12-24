class Solution:
    def sumZero(self, n: int) -> List[int]:  
        return ([-k for k in reversed(range(1, (n // 2) + 1))] + ([] if (n % 2 == 0) else [0]) + [k for k in range(1, (n // 2) + 1)]);
