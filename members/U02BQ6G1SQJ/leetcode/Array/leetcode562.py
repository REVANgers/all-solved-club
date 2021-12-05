import collections;
import math;

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """
        (answer, dp) = (0, [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]);
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if (mat[r][c] == 0):
                    continue;
                    
                minVal = math.inf;
                    
                if ((r > 0) and (mat[r - 1][c] == 1)):
                    # print("CASE 1");
                    
                    minVal = min(minVal, dp[r - 1][c]);
                    
                if ((c > 0) and (mat[r][c - 1] == 1)):
                    # print("CASE 2");
                    
                    minVal = min(minVal, dp[r][c - 1]);
                
                if ((r > 0) and (c > 0) and (mat[r - 1][c - 1] == 1)):
                    # print("CASE 3");
                    
                    minVal = min(minVal, dp[r - 1][c - 1]);
                    
                # print(r, c, minVal);
                # print();
                    
                dp[r][c] = (1 if (minVal == math.inf) else (minVal + 1));
                answer = max(answer, dp[r][c]);
        
        print(dp);
        
        return answer;
        """
        
        """
        if ((len(mat) == 1) and (len(mat[0]) == 1)):
            return mat[0][0];
        
        answer = 0;
        
        for r in range(len(mat)):
            oneCnt = mat[r][0];
            
            for c in range(1, len(mat[0])):
                if (mat[r][c] == 0):
                    oneCnt = 0;
                else:
                    oneCnt += 1;
                    answer = max(answer, oneCnt);
                           
                # print(r, c, oneCnt);
                    
        for c in range(len(mat[0])):
            oneCnt = mat[0][c];
            
            for r in range(1, len(mat)):
                if (mat[r][c] == 0):
                    oneCnt = 0;
                else:
                    oneCnt += 1;
                    answer = max(answer, oneCnt);
                           
                # print(r, c, oneCnt);
                    
        for diagonalSum in range(len(mat) + len(mat[0]) - 1):
            (oneCnt, isFirst) = (0, True);
            
            for r in range(diagonalSum + 1):
                c = diagonalSum - r;
                
                if (r >= len(mat)):
                    break;
                
                if (c >= len(mat[r])):
                    continue;
                
                # print(r, c);
                
                if (isFirst):
                    (oneCnt, isFirst) = (mat[r][c], False);
                    continue;
                    
                if (mat[r][c] == 0):
                    oneCnt = 0;
                else:
                    oneCnt += 1;
                    answer = max(answer, oneCnt);
                    
        for antiDiagonalDiff in range(-len(mat[0]) + 1, len(mat)):
            (oneCnt, isFirst) = (0, True);
            
            for c in range(-antiDiagonalDiff, len(mat[0])):
                r = antiDiagonalDiff + c;
                
                if (r >= len(mat)):
                    break;
                
                if (c < 0):
                    continue;
                
                # print(r, c);
                
                if (isFirst):
                    (oneCnt, isFirst) = (mat[r][c], False);
                    continue;
                    
                if (mat[r][c] == 0):
                    oneCnt = 0;
                else:
                    oneCnt += 1;
                    answer = max(answer, oneCnt);
                    
        return answer;
        """
        
        (answer, horizontalDict, verticalDict, diagonalDict, antiDiagonalDict) = (0, collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int));
        
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if (mat[r][c] == 0):
                    (horizontalDict[r], verticalDict[c], diagonalDict[r + c], antiDiagonalDict[r - c]) = (0, 0, 0, 0);
                else:
                    (horizontalDict[r], verticalDict[c], diagonalDict[r + c], antiDiagonalDict[r - c]) = (horizontalDict[r] + 1, verticalDict[c] + 1, diagonalDict[r + c] + 1, antiDiagonalDict[r - c] + 1);
                    answer = max(answer, horizontalDict[r], verticalDict[c], diagonalDict[r + c], antiDiagonalDict[r - c]);
                    
        return answer;
