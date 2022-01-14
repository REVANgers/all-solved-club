import collections;
import math;

HOUR_CNT = 24
MINUTE_CNT = 60;
MAX_TIME = ((HOUR_CNT * MINUTE_CNT) - 1);

def solution(fees : list, records : list) -> list:
    answerList = [];
    inDict = collections.defaultdict(list);
    outDict = collections.defaultdict(list);
    timeDict = collections.defaultdict(int);
    (baseTime, baseRate, unitTime, unitRate) = fees;

    for curRecord in records:
        (hourMinute, car, history) = curRecord.split(" ");
        (hour, minute) = hourMinute.split(":");
        time = int(hour) * MINUTE_CNT + int(minute);

        # print(hour, minute, time, car, history);

        timeDict[car] = 0;

        if (history == "IN"):
            inDict[car].append(time);
        elif (history == "OUT"):
            outDict[car].append(time);

    for curCar in timeDict.keys():
        for historyIdx in range(len(outDict[curCar])):
            timeDict[curCar] += (outDict[curCar][historyIdx] - inDict[curCar][historyIdx]);

        if (len(inDict[curCar]) != len(outDict[curCar])):
            timeDict[curCar] += (MAX_TIME - inDict[curCar][-1]);

    # print(inDict);
    # print(outDict);
    # print(timeDict);

    for curCar in sorted(timeDict.keys()):
        # print(curCar);

        if (timeDict[curCar] > baseTime):
            answerList.append(baseRate + (math.ceil((timeDict[curCar] - baseTime) / unitTime) * unitRate));
        else:
            answerList.append(baseRate);

    return answerList;
"""
print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT"]));
# [14600, 34400, 5000]
"""
"""
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN",
                "16:00 0202 IN",
                "18:00 3961 OUT",
                "18:00 0202 OUT",
                "23:58 3961 IN"]));
# [0, 591]
"""
"""
print(solution([1, 461, 1, 10],
               ["00:00 1234 IN"]));
# [14841]
"""
