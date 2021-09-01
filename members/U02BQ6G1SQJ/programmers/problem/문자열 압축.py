def solution(s):
    answer = len(s);
    
    # print(len(s));
    
    for compressionLen in range(1, (len(s) // 2) + 1):
        # print(compressionLen);
        
        (compressedStr, prevStr, strCnt) = ("", "", 0);
        
        for startIdx in range(0, len(s), compressionLen):
            endIdx = startIdx + compressionLen;
            curStr = s[startIdx : endIdx];
            
            # print(startIdx, endIdx, curStr);
            
            if (endIdx > len(s)):
                compressedStr += curStr;
                break;
                
            if (prevStr == curStr):
                strCnt += 1;
                continue;
            
            if (strCnt > 1):
                compressedStr += (str(strCnt) + prevStr);
            elif (strCnt == 1):
                compressedStr += prevStr;
                
            prevStr = curStr;
            strCnt = 1;
                
        if (strCnt > 1):
            compressedStr += (str(strCnt) + prevStr);
        elif (strCnt == 1):
            compressedStr += prevStr;
                
        # print(compressionLen, compressedStr);        
        
        answer = min(answer, len(compressedStr));
    
    return answer;
