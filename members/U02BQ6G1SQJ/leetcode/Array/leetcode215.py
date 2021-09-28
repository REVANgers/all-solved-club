class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, key = lambda v : -v)[k - 1];
