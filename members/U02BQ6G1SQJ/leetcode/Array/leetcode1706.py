# reference : https://leetcode.com/problems/where-will-the-ball-fall/discuss/988576/JavaC%2B%2BPython-Solution-with-Explanation

def checkBall(gridList : List[List[int]], ballIdx : int):
    for r in range(len(gridList)):
        c = ballIdx + gridList[r][ballIdx];
        
        if (c < 0) or (c >= len(gridList[0])) or (gridList[r][c] != gridList[r][ballIdx]):
            return -1;
        
        ballIdx = c;
    
    return ballIdx;

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        return [checkBall(grid, k) for k in range(len(grid[0]))];
