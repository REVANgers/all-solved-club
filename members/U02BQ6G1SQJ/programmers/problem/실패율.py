# 시험 당시 작성한 코드 : 시간 초과
"""
# 실패율

from operator import itemgetter;

def solution(N, stages):
    answer = [];

    # 성공한 횟수 배열
    success_list = [0 for i in range(N + 1)];

    # 도달 횟수 배열
    arrive_list = [0 for i in range(N + 1)];

    # 실패율 2차원 배열
    # 실패율, 스테이지
    failure_list = [[0] * 2 for i in range(N + 1)];

    # 하나씩 보면서 성공률 계산
    for i in stages:
        # 1번째부터 i - 1번째까지는 도달 & 성공
        for j in range(1, i):
            success_list[j] += 1;
            arrive_list[j] += 1;
        
        # 모두 성공한 상태 아니면
        if (i < N + 1):
            # i번째까지는 도달, 하지만 성공은 X
            arrive_list[i] += 1;

    # print(success_list);
    # print(arrive_list);

    # 실패율 배열 만들기
    for i in range(1, N + 1):
        # 0으로 나누는 경우
        if (arrive_list[i] == 0):
            # 실패율은 0
            failure_list[i][0] = 0;

        # 일반적인 경우
        else:
            # 실패율 공식
            failure_list[i][0] = (arrive_list[i] - success_list[i]) / arrive_list[i];

        # 몇 번째 스테이지인지 기록
        failure_list[i][1] = i;

    failure_list.sort(key = itemgetter(1));
    failure_list.sort(key = itemgetter(0), reverse = True);

    # print(failure_list);

    # 정답 배열 만들기
    for i in range(N + 1):
        answer.append(failure_list[i][1]);

    # 스테이지 0은 제거
    answer.remove(0);

    # print(answer);

    return answer;

# N = 5;
# stages = [2, 1, 2, 6, 2, 4, 3, 3];

# solution(N, stages);
"""

# 부스트캠프 이후 작성 코드
import collections;
import functools;

def fractionCompare(x : list, y : list) -> int:
    compareResult = (x[2] * y[1]) - (x[1] * y[2]);
    return ((x[0] - y[0]) if (compareResult == 0) else compareResult);

def solution(N : int, stages : list) -> list:
    (answerList, stagesCounter, remainCnt) = ([], collections.Counter(stages), len(stages));
    
    for curStage in range(1, N + 1):
        if (curStage in stagesCounter.keys()):
            failureCnt = stagesCounter[curStage];
            answerList.append([curStage, failureCnt, remainCnt]);
            remainCnt -= failureCnt;
        else:
            answerList.append([curStage, 0, 1]);
        
    # print(stagesCounter);
    # print(answerList);
    
    return [k[0] for k in sorted(answerList, key = functools.cmp_to_key(fractionCompare))];
