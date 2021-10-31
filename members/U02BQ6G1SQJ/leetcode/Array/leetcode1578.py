# reference : https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/discuss/831588/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        (answer, maxCost) = (0, 0);
        
        for chIdx in range(len(s)):
            if ((chIdx > 0) and (s[chIdx] != s[chIdx - 1])):
                maxCost = 0;
                
            answer += min(maxCost, cost[chIdx]);
            maxCost = max(maxCost, cost[chIdx]);
            
        return answer;
