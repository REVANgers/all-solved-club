import collections;

(SIZE_CNT, DICT_CNT) = (3, 4);

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        (rowPtsDict, colPtsDict, diagonalPtsDict, antiDiagonalPtsDict) = (collections.defaultdict(int) for _ in range(DICT_CNT));
        
        for moveIdx in range(len(moves)):
            (r, c) = moves[moveIdx];
            (curPts, retVal) = ((1, 'A') if (moveIdx % 2 == 0) else (-1, 'B'));
            (rowPtsDict[r], colPtsDict[c], diagonalPtsDict[r + c], antiDiagonalPtsDict[r - c]) = (rowPtsDict[r] + curPts, colPtsDict[c] + curPts, diagonalPtsDict[r + c] + curPts, antiDiagonalPtsDict[r - c] + curPts);
            
            if (SIZE_CNT in (abs(rowPtsDict[r]), abs(colPtsDict[c]), abs(diagonalPtsDict[r + c]), abs(antiDiagonalPtsDict[r - c]))):
                return retVal;
            
            # print("row :", rowPtsDict);
            # print("col :", colPtsDict);
            # print("diagonal :", diagonalPtsDict);
            # print();
        
        return ("Draw" if (len(moves) == SIZE_CNT ** 2) else "Pending");
