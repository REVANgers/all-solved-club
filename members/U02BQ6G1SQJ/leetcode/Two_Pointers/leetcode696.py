class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        answer = 0;
        
        for startIdx in range(len(s)):
            for endIdx in range(startIdx + 2, len(s) + 1, 2):
                # print(startIdx, endIdx, s[startIdx : endIdx]);
                
                midIdx = (startIdx + endIdx) // 2;
                (leftSet, rightSet) = (set(s[startIdx : midIdx]), set(s[midIdx : endIdx]));
                
                # print(leftSet, rightSet, s[startIdx : midIdx], s[midIdx : endIdx]);
                
                if ((leftSet, rightSet) in (({'0'}, {'1'}), ({'1'}, {'0'}))):
                    # print("O");
                    
                    answer += 1;
                    
        return answer;
        """
        
        (answer, prevNum, curNum) = (0, 0, 1);
        
        for chIdx in range(1, len(s)):
            if (s[chIdx] != s[chIdx - 1]):
                answer += min(prevNum, curNum);
                (prevNum, curNum) = (curNum, 1);
            else:
                curNum += 1;
                
        return (answer + min(prevNum, curNum));
