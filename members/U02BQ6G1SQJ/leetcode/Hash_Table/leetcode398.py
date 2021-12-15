import collections;
import random;

class Solution:
    def __init__(self, nums: List[int]):
        self.numDict = collections.defaultdict(list);
        
        for numIdx in range(len(nums)):
            self.numDict[nums[numIdx]].append(numIdx);
        
        # print(self.numDict);

    def pick(self, target: int) -> int:
        return random.choice(self.numDict[target]);

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
