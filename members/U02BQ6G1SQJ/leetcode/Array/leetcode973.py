class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda k : (k[0] ** 2 + k[1] ** 2))[ : k];
