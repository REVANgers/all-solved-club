DIGIT = 10;

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [];
        
        for curCh in s:
            if (curCh == "]"):
                (k, curDigit, curStr) = (0, 1, "");
                
                while ((stack) and (stack[-1].isalpha())):
                    curStr = stack.pop() + curStr;
                    
                stack.pop();
                
                while ((stack) and (stack[-1].isdigit())):
                    k += (curDigit * int(stack.pop()));
                    curDigit *= DIGIT;
                
                # print(k, curStr);
                
                for pushIdx in range(k):
                    stack.extend(list(curStr));
            else:
                stack.append(curCh);
                
            # print(stack);
            
        return "".join(stack);
