def solution(weights, head2head):
    answerList = [];
    
    for r in range(len(head2head)):
        (winCnt, matchCnt, heavyCnt) = (0, 0, 0);
        
        for c in range(len(head2head)):
            if (head2head[r][c] == "W"):
                winCnt += 1;
                matchCnt += 1;
                
                if (weights[r] < weights[c]):
                    heavyCnt += 1;
                
            elif (head2head[r][c] == "L"):
                matchCnt += 1;
        
        winRate = (0 if (matchCnt == 0) else (winCnt / matchCnt));
        
        # print(winCnt, matchCnt, winRate, heavyCnt);
        
        answerList.append([r + 1, winRate, heavyCnt, weights[r]]);
    
    # print(answerList);
    
    return [k[0] for k in sorted(answerList, key = lambda k : (-k[1], -k[2], -k[3], k[0]))];
