import math;

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        (rows, cols) = binaryMatrix.dimensions();
        (minIdx, minVal) = (math.inf, math.inf);
        leftmostColumnList = [math.inf for _ in range(cols)];
        
        # print(rows, cols);
        
        for r in range(rows):
            (left, right) = (0, cols - 1);
            
            while (left <= right):
                mid = (left + right) // 2;
                val = binaryMatrix.get(r, mid);
                
                if (val == 0):
                    left = mid + 1;
                else:
                    (leftmostColumnList[r], right) = (mid, mid - 1);
                    
        # print(leftmostColumnList);
        
        for c in range(cols):
            if (minVal > leftmostColumnList[c]):
                (minIdx, minVal) = (c, leftmostColumnList[c]);
                
                # print(minIdx, minVal);
                
        return (-1 if (minVal == math.inf) else minVal);
