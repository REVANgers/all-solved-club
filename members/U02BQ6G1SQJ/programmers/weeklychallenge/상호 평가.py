DIGIT = 10;
GRADE_LIST = ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A'];

def solution(scores):
    answer = '';
    transposedScores = list(zip(*scores));
    
    for studentIdx in range(len(scores)):
        studentScoreList = transposedScores[studentIdx];
        selfScore = studentScoreList[studentIdx];
        
        if ((selfScore in [min(studentScoreList), max(studentScoreList)]) 
                               and (studentScoreList.count(selfScore) == 1)):
            answer += GRADE_LIST[((sum(studentScoreList) - selfScore) // (len(scores) - 1)) // DIGIT];
        else:
            answer += GRADE_LIST[(sum(studentScoreList) // len(scores)) // DIGIT];  
            
    return answer;
