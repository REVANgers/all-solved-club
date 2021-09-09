# 소요 시간 : 120분 (실패)
# 문제 풀이 reference : https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
import datetime;
import itertools;

# HOUR_CNT = 24;
HOUR_CNT = 100;
MINUTE_CNT = 60;
SECOND_CNT = 60;
TIME_CNT = HOUR_CNT * MINUTE_CNT * SECOND_CNT;

def hourToDay(hour : int) -> int:
    return divmod(hour, HOUR_CNT);

def getTimedelta(timeStr : str) -> datetime.timedelta:
    timeList = timeStr.split(":");
    (day, hour) = hourToDay(int(timeList[0]));
    (minute, second) = (int(timeList[1]), int(timeList[2]));
    
    # print(datetime.timedelta(days = day, hours = hour, minutes = minute, seconds = second));
    
    return datetime.timedelta(days = day, hours = hour, minutes = minute, seconds = second);

def getAccumulateTimedelta(videoStartDatetime : datetime.datetime, videoEndDatetime : datetime.datetime, advStartDatetime : datetime.datetime, advEndDatetime : datetime.datetime, startIdx : int, logDatetimeList : list) -> datetime.timedelta:
    accumulateTimedelta = datetime.timedelta();
    
    # print("start :", startIdx, advStartDatetime, advEndDatetime);
    
    for logIdx in range(len(logDatetimeList)):
        (logStartDatetime, logEndDatetime) = logDatetimeList[logIdx];
        
        # print("log :", logIdx, logStartDatetime, logEndDatetime);
        
        if (logEndDatetime <= advStartDatetime):
            continue;
        
        if (logStartDatetime >= advEndDatetime):
            break;
        
        accumulateTimedelta += (min(advEndDatetime, logEndDatetime) - max(advStartDatetime, logStartDatetime));
        
        # print(accumulateTimedelta);
    
    return accumulateTimedelta;

def strToSecond(timeStr : str) -> int:
    (hour, minute, second) = list(map(int, timeStr.split(":")));
    return ((hour * MINUTE_CNT * SECOND_CNT) + (minute * SECOND_CNT) + second);

def secondToStr(timeSecond : int) -> str:
    (hourMinute, second) = divmod(timeSecond, SECOND_CNT);
    (hour, minute) = divmod(hourMinute, MINUTE_CNT);
    return ("%02d:%02d:%02d" % (hour, minute, second));

def solution(play_time : str, adv_time : str, logs : list) -> str:
    """
    1. 시작 시간 순서대로 정렬하여 로그별 탐색 : 실패
    videoStartDatetime = datetime.datetime.today();
    videoEndDatetime = videoStartDatetime + getTimedelta(play_time);
    advTimedelta = getTimedelta(adv_time);
    sortedLogList = list(map(lambda k : k.split("-"), sorted(logs)));
    logDatetimeList = [];
    advStartDatetimeSet = set();
    
    # print(videoStartDatetime, videoEndDatetime);
    # print(sortedLogList);
    
    for (startStr, endStr) in sortedLogList:
        (logStartDatetime, logEndDatetime) = (videoStartDatetime + getTimedelta(startStr), videoStartDatetime + getTimedelta(endStr));
        
        # print(startStr, endStr);
        # print(logStartDatetime, logEndDatetime);
        
        logDatetimeList.append([logStartDatetime, logEndDatetime]);
        
    # print(logDatetimeList);
    
    answerLogIdx = -1;
    advStartDatetime = videoStartDatetime;
    advEndDatetime = advStartDatetime + advTimedelta;
    maxAccumulateTimedelta = getAccumulateTimedelta(videoStartDatetime, videoEndDatetime, advStartDatetime, advEndDatetime, answerLogIdx, logDatetimeList);
    
    # print(answerLogIdx, maxAccumulateTimedelta, advTimedelta);
    
    for logIdx in range(len(logDatetimeList)):
        advStartDatetime = logDatetimeList[logIdx][0];
        
        if (advStartDatetime in advStartDatetimeSet):
            continue;
        
        advEndDatetime = advStartDatetime + advTimedelta;
        
        if (advEndDatetime > videoEndDatetime):
            break;
        
        curAccumulateTimedelta = getAccumulateTimedelta(videoStartDatetime, videoEndDatetime, advStartDatetime, advEndDatetime, logIdx, logDatetimeList);
        
        # print(logIdx, curAccumulateTimedelta);
        
        if (maxAccumulateTimedelta < curAccumulateTimedelta):
            (answerLogIdx, maxAccumulateTimedelta) = (logIdx, curAccumulateTimedelta);
            
    # print(answerLogIdx, maxAccumulateTimedelta, advTimedelta);
    # print(sortedLogList[answerLogIdx][0]);
    
    return ("00:00:00" if (answerLogIdx == -1) else sortedLogList[answerLogIdx][0]);
    """
    
    # 2. 모든 시각을 초로 환산한 후 시각별 탐색
    # 문제를 쉽게 해결하려면, 등장하는 모든 시각을 초로 환산하여 접근하는 것이 필요합니다. 
    # play_time이 99시 59분 59초이하가 되므로, 문제에서 나올 수 있는 모든 시각의 개수는 100 * 60 * 60 = 360000개를 넘지 않습니다.
    
    # STEP 1. 매개변수로 주어진 play_time, adv_time, logs에 대해서, 시각을 초로 환산하여 아래와 같이 저장합니다.
    logList = list(map(lambda k : k.split("-"), logs));
    # logs_start_sec[i] = logs[i]의 시작 시각을 초로 환산한 값
    # logs_end_sec[i] = logs[i]의 종료 시각을 초로 환산한 값
    (logStartSecondList, logEndSecondList) = (list(zip(*list(map(lambda k : [strToSecond(k[0]), strToSecond(k[1])], logList)))));
    # play_time_sec = play_time을 초로 환산한 값
    # adv_time_sec = adv_time을 초로 환산한 값
    (playTimeSecond, advTimeSecond) = (strToSecond(play_time), strToSecond(adv_time));
    
    # print(logList);
    # print(logStartSecondList, logEndSecondList);
    # print(playTimeSecond, advTimeSecond);
    # print(secondToStr(playTimeSecond), secondToStr(advTimeSecond));
    
    # STEP 2. 다음과 같이 total_time 배열을 정의합니다.
    # total_time[x] = x 시각에 시작된 재생 구간의 개수 – x 시각에 종료된 재생구간의 개수
    totalTimeList = [0 for _ in range(TIME_CNT)];
    
    # 이렇게 정의한 total_time 배열은 STEP 1.에서 만든 logs_start_sec과 logs_end_sec 배열을 사용하여 구해줄 수 있습니다.
    # for i = 0 ~ logs의 마지막 인덱스
        # total_time[logs_start_sec[i]] = total_time[logs_start_sec[i]] + 1
        # total_time[logs_end_sec[i]] = total_time[logs_end_sec[i]] - 1
    for logIdx in range(len(logs)):
        totalTimeList[logStartSecondList[logIdx]] += 1;
        totalTimeList[logEndSecondList[logIdx]] -= 1;
    
    # STEP 3. 다음과 같이 total_time 배열을 재정의합니다.
    # total_time[x] = 시각 x부터 x+1까지 1초 간의 구간을 포함하는 재생 구간의 개수
    # 재정의된 total_time 배열은 STEP 2.에서 만든 기존의 total_time 배열을 이용하여 계산할 수 있습니다.
    # for i = 1 ~ (play_time_sec - 1)
        # total_time[i] = total_time[i] + total_time[i - 1]
    totalTimeList = list(itertools.accumulate(totalTimeList));
        
    # STEP 4.
    # 다음과 같이 total_time 배열을 재정의합니다.
    # total_time[x] = 시각 0부터 x+1까지 x+1초 간의 구간을 포함하는 누적 재생시간
    # 재정의된 total_time 배열은 STEP 3.에서 만든 기존의 total_time 배열을 이용하고, 완전히 똑같은 반복문을 한 번 더 실행하면 구해줄 수 있습니다.
    # for i = 1 ~ (play_time_sec - 1)
        # total_time[i] = total_time[i] + total_time[i - 1]
    totalTimeList = list(itertools.accumulate(totalTimeList));
        
    # STEP 5.
    # 마지막으로 정답을 구하는 과정입니다.
    # for i = (adv_time_sec - 1) ~ (play_time_sec - 1)
        # if ( i >= at) 
            # max_time = max(max_time, total_time[i] - total_time[i - at] )
        # else 
            # max_time = max(max_time, total_time[i])    
    # 위 코드는 반복문을 돌며 시각 i - at + 1에 광고를 넣을 때의 누적 재생 시간을 구하여, 그중에서 가장 긴 시간을 max_time에 넣어주고 있습니다. 
    # max_time 값이 마지막으로 업데이트될 때의 시각 i - at + 1을 HH:MM:SS 형태로 변환한 값이 문제에서 요구하는 정답입니다.
    (answerSecond, maxTime) = (0, 0);
    
    for secondIdx in range(advTimeSecond - 1, playTimeSecond):
        if (secondIdx >= advTimeSecond):
            curTime = totalTimeList[secondIdx] - totalTimeList[secondIdx - advTimeSecond];
            
            if (maxTime < curTime):
                (answerSecond, maxTime) = (secondIdx - advTimeSecond + 1, max(maxTime, curTime));
        else:
            maxTime = max(maxTime, totalTimeList[secondIdx]);
        
    # print(secondToStr(answerSecond), answerSecond, maxTime);
    
    return secondToStr(answerSecond);
