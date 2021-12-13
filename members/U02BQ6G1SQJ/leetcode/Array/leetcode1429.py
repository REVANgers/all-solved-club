import collections;

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.dq = collections.deque();
        self.uniqueSet = set();
        self.nonUniqueSet = set();
        
        for curNum in nums:
            self.add(curNum);
                
        # print(self.dq);
        # print(self.uniqueSet);
        # print(self.nonUniqueSet);

    def showFirstUnique(self) -> int:
        while (self.dq):
            curNum = self.dq.popleft();
            
            if (curNum in self.nonUniqueSet):
                continue;
                
            if (curNum in self.uniqueSet):
                self.dq.appendleft(curNum);
                return curNum;
        
        return -1;

    def add(self, value: int) -> None:
        if (value in self.nonUniqueSet):
            return None;
                
        if (value in self.uniqueSet):
            self.uniqueSet.remove(value);
            self.nonUniqueSet.add(value);
        else:
            self.dq.append(value);
            self.uniqueSet.add(value);
        
        return None;

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
