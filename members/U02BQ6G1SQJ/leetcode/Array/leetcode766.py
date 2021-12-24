import collections;

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        toeplitzDict = collections.defaultdict(set);
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):                
                toeplitzDict[r - c].add(matrix[r][c]);
                
                if (len(toeplitzDict[r - c]) > 1):
                    return False;
                
        return True;
