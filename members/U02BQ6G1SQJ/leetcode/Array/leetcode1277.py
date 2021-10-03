class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        (answer, maxSide, prefixSumList) = (0, 0, [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]);
        
        for r in range(len(matrix)):
            curSide = 0;
            
            for c in range(len(matrix[r])):
                if (matrix[r][c] == 0):
                    curSide = 0;
                else:
                    curSide += 1;
                    maxSide = max(maxSide, curSide);
                
                if ((r == 0) and (c == 0)):
                    prefixSumList[r][c] = matrix[r][c];
                elif (r == 0):
                    prefixSumList[r][c] = prefixSumList[r][c - 1] + matrix[r][c];
                elif (c == 0):
                    prefixSumList[r][c] = prefixSumList[r - 1][c] + matrix[r][c];
                else:
                    prefixSumList[r][c] = prefixSumList[r - 1][c] + prefixSumList[r][c - 1] - prefixSumList[r - 1][c - 1] + matrix[r][c];
                    
        for c in range(len(matrix[r])):
            curSide = 0;
            
            for r in range(len(matrix)):
                if (matrix[r][c] == 0):
                    curSide = 0;
                else:
                    curSide += 1;
                    maxSide = max(maxSide, curSide);
                    
        # print(prefixSumList);
        
        for curSide in range(1, maxSide + 1):
            for endR in range(curSide - 1, len(matrix)):
                for endC in range(curSide - 1, len(matrix[0])):
                    (curSum, startR, startC) = (0, endR - curSide, endC - curSide);
                    
                    if ((startR == -1) and (startC == -1)):
                        curSum = prefixSumList[endR][endC];
                    elif (startR == -1):
                        curSum = prefixSumList[endR][endC] - prefixSumList[endR][startC];
                    elif (startC == -1):
                        curSum = prefixSumList[endR][endC] - prefixSumList[startR][endC];
                    else:
                        curSum = prefixSumList[endR][endC] - prefixSumList[startR][endC] - prefixSumList[endR][startC] + prefixSumList[startR][startC];
                        
                    # print("start :", startR, startC);
                    # print("end :", endR, endC);
                    # print(curSum);
                        
                    if (curSum == curSide ** 2):
                        answer += 1;
                    
            # print();
            
        return answer;
