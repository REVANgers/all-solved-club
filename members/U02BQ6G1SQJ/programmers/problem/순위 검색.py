# 소요 시간 : 49분
import itertools;

LANGUAGE_LIST = ["-", "cpp", "java", "python"];
JOB_LIST = ["-", "backend", "frontend"];
CAREER_LIST = ["-", "junior", "senior"];
FOOD_LIST = ["-", "chicken", "pizza"];

def solution(info, query):
    (answerList, infoList) = ([], []);
    productList = list(itertools.product(LANGUAGE_LIST, JOB_LIST, CAREER_LIST, FOOD_LIST));
    queryDict = dict(zip(productList, [[] for _ in range(len(productList))]));
    
    for infoStr in info:
        (language, job, career, food, score) = infoStr.split(" ");
        
        # print(language, job, career, food, score);
        
        for p in itertools.product(["-", language], ["-", job], ["-", career], ["-", food]):
            # print(p);
            
            queryDict[p].append(int(score));
    
    for queryVal in queryDict.values():
        queryVal.sort();
        
    # print(infoList);
    # print(productList);
    # print(queryDict);
    
    for queryStr in query:
        queryList = queryStr.split(" ");
        (queryKey, score) = ((queryList[0], queryList[2], queryList[4], queryList[6]), int(queryList[7]));
        (answer, left, right) = (len(queryDict[queryKey]), 0, len(queryDict[queryKey]) - 1);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            # print(mid, left, right);
            # print(queryDict[queryKey][mid], queryDict[queryKey][left], queryDict[queryKey][right]);
            
            if (queryDict[queryKey][mid] < score):
                left = mid + 1;
            else:
                (answer, right) = (mid, mid - 1);
        
        answerList.append(len(queryDict[queryKey]) - answer);
    
    return answerList;
