import itertools;

DIGIT = 10;
OPERATOR_LIST = ["+", "-", "*"];

def infixToPostfix(infixStr : str, operatorDict : dict) -> list:
    (postfixList, stack, curNum) = ([], [], 0);
    
    for curCh in infixStr:
        if (curCh.isdigit()):
            curNum = (curNum * DIGIT) + int(curCh);
            continue;
            
        postfixList.append(str(curNum));
        curNum = 0;
        
        while ((stack) and (operatorDict[stack[-1]] >= operatorDict[curCh])):
            postfixList.append(stack.pop());
            
        stack.append(curCh);
    
    postfixList.append(str(curNum));
    
    while (stack):
        postfixList.append(stack.pop());
        
    # print(postfixList);
    # print(stack);
    
    return postfixList;
    
def calculatePostFix(postfixList : list) -> int:
    (stack, result) = ([], 0);
    
    for curStr in postfixList:
        if (curStr.isdigit()):
            stack.append(curStr);
            continue;
            
        (num2, num1) = (int(stack.pop()), int(stack.pop()));
        
        if (curStr == "+"):
            stack.append(num1 + num2);
        elif (curStr == "-"):
            stack.append(num1 - num2);
        elif (curStr == "*"):
            stack.append(num1 * num2);
    
    # print(stack[-1]);
    
    return abs(stack[-1]);

def solution(expression):
    answer = 0;
    
    for p in itertools.permutations([k for k in range(len(OPERATOR_LIST))], len(OPERATOR_LIST)):
        # print(dict(zip(OPERATOR_LIST, p)));
        
        answer = max(answer, calculatePostFix(infixToPostfix(expression, dict(zip(OPERATOR_LIST, p)))));
    
    return answer;
