import collections;

LANGUAGE_CNT = 5;

def solution(table : list, languages : list, preference : list) -> str:
    answerList = [];
    jobDict = {"SI" : collections.defaultdict(int), 
               "CONTENTS" : collections.defaultdict(int), 
               "HARDWARE" : collections.defaultdict(int), 
               "PORTAL" : collections.defaultdict(int), 
               "GAME" : collections.defaultdict(int)};
    
    for languageStr in table:
        languageList = languageStr.split();
        
        for languageIdx in range(1, LANGUAGE_CNT + 1):
            jobDict[languageList[0]][languageList[languageIdx]] = LANGUAGE_CNT - languageIdx + 1;
    
    for curJob in jobDict.keys():
        for languageIdx in range(len(languages)):
            jobDict[curJob]["POINT"] += jobDict[curJob][languages[languageIdx]] * preference[languageIdx];
            
        answerList.append([curJob, jobDict[curJob]["POINT"]]);
            
    # print(jobDict);
    
    return sorted(answerList, key = lambda k : (-k[1], k[0]))[0][0];
