# reference : https://leetcode.com/problems/new-21-game/discuss/132334/One-Pass-DP-O(N)

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if ((k == 0) or (n >= k + maxPts)):
            return 1.0;
        
        (dp, ptsSum) = ([1.0], 1.0);
        
        for curNum in range(1, n + 1):
            dp.append(ptsSum / maxPts);
            
            if (curNum < k):
                ptsSum += dp[curNum];
                
            if (curNum >= maxPts):
                ptsSum -= dp[curNum - maxPts];
                
        return sum(dp[k : ]);
