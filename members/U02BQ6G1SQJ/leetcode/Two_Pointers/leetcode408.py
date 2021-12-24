DIGIT = 10;

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        (abbrList, tmpNum, chIdx) = ([], 0, 0);
        
        for curCh in abbr:
            if (curCh.isdigit()):
                if ((tmpNum == 0) and (curCh == '0')):
                    return False;
                
                tmpNum = (tmpNum * DIGIT) + int(curCh);
            else:
                if (tmpNum != 0):
                    abbrList.append(str(tmpNum));
                    tmpNum = 0;
                
                abbrList.append(curCh);
        
        if (tmpNum > 0):
            abbrList.append(str(tmpNum));
        
        # print(abbrList);
        
        for curCh in abbrList:
            # print(curCh, word[chIdx]);
            
            if (curCh.isdigit()):
                chIdx += int(curCh);
            else:
                if ((chIdx >= len(word)) or (curCh != word[chIdx])):
                    return False;
                
                chIdx += 1;
        
        return (chIdx == len(word));
