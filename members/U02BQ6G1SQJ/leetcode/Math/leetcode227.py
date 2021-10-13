(DIGIT, OPERATOR_DICT, OPERATOR_SET) = (10, {"+" : 1, "-" : 1, "*" : 2, "/" : 2}, set(["+", "-", "*", "/"]));

def infixToPostfix(infixStr : str) -> str:
    (postfixList, stack, curNum) = ([], [], 0);
    
    for curCh in infixStr:
        if (curCh.isdigit()):
            curNum = (curNum * DIGIT) + int(curCh);
        elif (curCh in OPERATOR_SET):
            postfixList.append(curNum);
            curNum = 0;
            
            while ((stack) and (OPERATOR_DICT[curCh] <= OPERATOR_DICT[stack[-1]])):
                postfixList.append(stack.pop());
                
            stack.append(curCh);
            
    postfixList.append(curNum);
            
    while (stack):
        postfixList.append(stack.pop());
            
    return postfixList;

def calculatePostfix(postfixList : list) -> int:
    stack = [];
    
    for curElement in postfixList:
        if (curElement in OPERATOR_SET):
            (val2, val1) = (stack.pop(), stack.pop());
            
            if (curElement == "+"):
                stack.append(val1 + val2);
            elif (curElement == "-"):
                stack.append(val1 - val2);
            elif (curElement == "*"):
                stack.append(val1 * val2);
            elif (curElement == "/"):
                stack.append(val1 // val2);
        else:
            stack.append(curElement);
                
    return stack[0];

class Solution:
    def calculate(self, s: str) -> int:
        return calculatePostfix(infixToPostfix(s));
