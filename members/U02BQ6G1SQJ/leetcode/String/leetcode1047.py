def checkDuplicates(s : str) -> str:
    """
    (newStr, chIdx) = ("", 0);
    
    while (chIdx < len(s)):
        if (chIdx < len(s) - 1) and (s[chIdx] == s[chIdx + 1]):
            chIdx += 2;
        else:
            (newStr, chIdx) = (newStr + s[chIdx], chIdx + 1);
            
    return newStr;
    """
    
    stack = [];
    
    for curCh in s:
        if ((stack) and (curCh == stack[-1])):
            stack.pop();
        else:
            stack.append(curCh);
            
    return "".join(stack);
    
class Solution:
    def removeDuplicates(self, s: str) -> str:
        while (True):
            checkStr = checkDuplicates(s);
        
            if (s == checkStr):
                return checkStr;
            
            s = checkStr;
            
        return s;
