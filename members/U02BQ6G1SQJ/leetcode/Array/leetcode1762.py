class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [];
        
        for heightIdx in range(len(heights)):
            while ((stack) and (heights[heightIdx] >= stack[-1][1])):
                stack.pop();
                
            stack.append([heightIdx, heights[heightIdx]]);
            
        # print(stack);
        
        return [k[0] for k in stack];
