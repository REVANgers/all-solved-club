import collections;

DIR_DICT = {"U" : (-1, 0), "D" : (1, 0), "L" : (0, -1), "R" : (0, 1)};

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.foodIdx = 0;
        self.width = width;
        self.height = height;
        self.foodList = food;
        self.posSet = set([tuple([0, 0])]);
        self.dq = collections.deque([[0, 0]]);

    def move(self, direction: str) -> int:
        (curR, curC) = self.dq[-1];
        (dr, dc) = DIR_DICT[direction];
        (nextR, nextC) = (curR + dr, curC + dc);
        
        if ((nextR < 0) or (nextR >= self.height) or (nextC < 0) or (nextC >= self.width)):
            return -1;
        
        if ((self.foodIdx < len(self.foodList)) and ([nextR, nextC] == self.foodList[self.foodIdx])):
            self.foodIdx += 1;
        else:
            self.posSet.remove(tuple(self.dq.popleft()));
            
        posTuple = tuple([nextR, nextC]);
        
        if (posTuple in self.posSet):
            return -1;
        
        self.posSet.add(posTuple);
        self.dq.append([nextR, nextC]);
        
        # print(nextR, nextC, self.foodList[self.foodIdx]);  
        # print(self.dq);
            
        return (len(self.dq) - 1);

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
