MOD = (10 ** 9) + 7;

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        (sortedHorizontalCutList, sortedVerticalCutList) = (sorted(horizontalCuts), sorted(verticalCuts));
        (maxH, maxW) = (max(sortedHorizontalCutList[0], h - sortedHorizontalCutList[-1]), max(sortedVerticalCutList[0], w - sortedVerticalCutList[-1]));
        
        for i in range(len(sortedHorizontalCutList) - 1):
            maxH = max(maxH, sortedHorizontalCutList[i + 1] - sortedHorizontalCutList[i]);
            
        for j in range(len(sortedVerticalCutList) - 1):
            maxW = max(maxW, sortedVerticalCutList[j + 1] - sortedVerticalCutList[j]);
            
        return ((maxH * maxW) % MOD);
