class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        (answerStr, stack, removeList, startIdx) = ("", [], [], 0);
        
        for chIdx in range(len(s)):
            if (s[chIdx] == "("):
                stack.append(chIdx);
            elif (s[chIdx] == ")"):
                if (stack):
                    stack.pop();
                else:
                    removeList.append(chIdx);
            
        removeList += stack;
        
        for chIdx in sorted(removeList):
            answerStr += s[startIdx : chIdx];
            startIdx = chIdx + 1;
            
        answerStr += s[startIdx : ];
        
        # print(answerStr);
        # print(stack);
        # print(removeList);
                
        return answerStr;
