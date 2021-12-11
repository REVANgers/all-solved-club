class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        (answerStr, chIdx, commentFlag, sourceStr) = ("", 0, 0, "\\n".join(source));
        
        while (chIdx < len(sourceStr)):
            if (commentFlag == 0):
                # print("Text :", sourceStr[chIdx]);
                
                if ((chIdx < len(sourceStr) - 1) and (sourceStr[chIdx : chIdx + 2] == "//")):
                    # print(commentFlag, sourceStr[chIdx : chIdx + 2]);
                    
                    (chIdx, commentFlag) = (chIdx + 2, 1);
                elif ((chIdx < len(sourceStr) - 1) and (sourceStr[chIdx : chIdx + 2] == "/*")):
                    # print(commentFlag, sourceStr[chIdx : chIdx + 2]);
                    
                    (chIdx, commentFlag) = (chIdx + 2, 2);
                else:
                    answerStr += sourceStr[chIdx];
                    chIdx += 1;
                    
                    # print(answerStr);
            elif (commentFlag == 1):
                if ((chIdx < len(sourceStr) - 1) and (sourceStr[chIdx : chIdx + 2] == "\\n")):
                    # print(commentFlag, sourceStr[chIdx : chIdx + 2]);
                    
                    (answerStr, chIdx, commentFlag) = (answerStr + "\\n", chIdx + 2, 0);
                else:
                    chIdx += 1;
            elif (commentFlag == 2):
                if ((chIdx < len(sourceStr) - 1) and (sourceStr[chIdx : chIdx + 2] == "*/")):
                    # print(commentFlag, sourceStr[chIdx : chIdx + 2]);
                    
                    (chIdx, commentFlag) = (chIdx + 2, 0);
                else:
                    chIdx += 1;
        
        # print(answerStr);
        
        return list(filter(lambda k : k, answerStr.split("\\n")));
