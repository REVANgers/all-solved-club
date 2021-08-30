def compareSection(a : list, b : list) -> int:
    (aLen, bLen) = (a[1] - a[0] + 1, b[1] - b[0] + 1);
    return ((a[0] - b[0]) if (aLen == bLen) else (aLen - bLen));

def solution(gems):
    (answerList, gemDict, gemSet, left, right) = ([1, len(gems)], {gems[0] : 1}, set(gems), 0, 0);
    
    # print(gemSet);
    
    while (left < len(gems)):
        curGem = gems[right];
        
        # print(left, right, curGem);

        if (len(gemDict) == len(gemSet)) or (right == len(gems) - 1):
            sectionList = [left + 1, right + 1];
            
            if ((len(gemDict) == len(gemSet) and (compareSection(sectionList, answerList) < 0))):
                answerList = sectionList;
                
            leftGem = gems[left];
            gemDict[leftGem] -= 1;
            
            if (gemDict[leftGem] == 0):
                del gemDict[leftGem];
            
            left += 1;
        else:
            right += 1;
            rightGem = gems[right];
            
            if (rightGem not in gemDict.keys()):
                gemDict[rightGem] = 1;
            else:
                gemDict[rightGem] += 1;
    
    return answerList;
