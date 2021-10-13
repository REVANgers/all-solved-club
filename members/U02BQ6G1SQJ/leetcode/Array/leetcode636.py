class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        (answerList, stack, curFunctionID, curTimestamp) = ([0 for _ in range(n)], [], -1, 0);
        
        for curLog in logs:
            (functionID, message, timestamp) = curLog.split(":");
            (functionID, timestamp) = (int(functionID), int(timestamp));
            
            # print(functionID, message, timestamp);
            
            if (message == "start"):
                stack.append([functionID, timestamp]);
                
                if (curFunctionID != -1):
                    answerList[curFunctionID] += (timestamp - curTimestamp);
                    
                (curFunctionID, curTimestamp) = (functionID, timestamp);
            elif (message == "end"):
                (startFunctionID, startTimestamp) = stack.pop();
                answerList[curFunctionID] += (timestamp - curTimestamp + 1);
                (curFunctionID, curTimestamp) = ((stack[-1][0] if (stack) else -1), timestamp + 1);
        
        return answerList;
