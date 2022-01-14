import collections;

def solution(id_list : list, report : list, k : int) -> list:
    answerList = [];
    idSet = set();
    reportDict = collections.defaultdict(set);
    reportCounter = collections.Counter();

    for curReport in report:
        (src, dst) = curReport.split(" ");

        if (dst not in reportDict[src]):
            reportDict[src].add(dst);
            reportCounter[dst] += 1;

            if (reportCounter[dst] >= k):
                idSet.add(dst);

    # print(idSet);
    # print(reportDict);
    # print(reportCounter);

    for curId in id_list:
        if (curId in reportDict.keys()):
            answerList.append(len(reportDict[curId] & idSet));
        else:
            answerList.append(0);

    return answerList;

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)); # [2,1,1,0]
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3));                                      # [0,0]
