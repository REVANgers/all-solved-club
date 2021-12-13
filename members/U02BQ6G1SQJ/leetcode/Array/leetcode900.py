import collections;

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.dq = collections.deque();
        
        for encodingIdx in range(0, len(encoding), 2):
            self.dq.append(encoding[encodingIdx : encodingIdx + 2]);
            
        # print(self.dq);    

    def next(self, n: int) -> int:
        # print(self.dq);
        
        while (self.dq):
            (cnt, num) = self.dq.popleft();
            
            if (n > cnt):
                n -= cnt;
            else:
                self.dq.appendleft([cnt - n, num]);
                return num;
            
        return -1;

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
