import random;

class Solution:
    def __init__(self, w: List[int]):
        """
        self.randomList = [];
        
        for numIdx in range(len(w)):
            self.randomList.extend([numIdx] * w[numIdx]);
        
        # print(self.randomList);
        """
        
        wSum = sum(w);
        self.indexList = [k for k in range(len(w))];
        self.weightList = [(k / wSum) for k in w];

    def pickIndex(self) -> int:
        # return random.choice(self.randomList);
        
        return random.choices(self.indexList, self.weightList)[0];

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
