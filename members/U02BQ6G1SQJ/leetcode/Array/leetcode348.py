def checkFinished(n : int, score : int, index : int, sumList : list) -> bool:
    sumList[index] += score;
    return (sumList[index] == score * n);

class TicTacToe:
    def __init__(self, n: int):
        self.n = n;
        self.horizontalSumList = [0 for _ in range(n)];
        self.verticalSumList = [0 for _ in range(n)];
        self.diagonalSumList = [0, 0];

    def move(self, row: int, col: int, player: int) -> int:
        score = (1 if (player == 1) else -1);
        
        if (checkFinished(self.n, score, row, self.horizontalSumList)):
            return player;
        
        if (checkFinished(self.n, score, col, self.verticalSumList)):
            return player;
        
        if ((row == col) and (checkFinished(self.n, score, 0, self.diagonalSumList))):
            return player;
            
        if ((row + col == self.n - 1) and (checkFinished(self.n, score, 1, self.diagonalSumList))):
            return player;
            
        return 0;

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
