# 시험 당시 작성한 코드 : 시간 초과
"""
# 무지의 먹방 라이브

def solution(food_times, k):
    answer = 0;

    # 현재 걸린 시간
    cur_time = 0;

    # 현재 먹는 음식
    cur_index = 0;

    while (True):
        # print(food_times);
        # print(cur_time);

        # 다 먹었으면
        if (max(food_times) == 0):
            # 먹을 게 없다
            answer = -1;
            # 종료
            break;

        # 네트워크 장애 시간이면
        if ((cur_time == k) and food_times[cur_index] > 0):
            # 해당 음식부터 다시 먹는다
            answer = cur_index + 1;
            # 종료
            break;

        # 음식이 있으면
        if (food_times[cur_index] > 0):
            # 먹는다
            food_times[cur_index] -= 1;

            # 넘어간다
            cur_index += 1;

            # 시간도 걸린다
            cur_time += 1;
            
        # 음식이 없으면
        else:
            # 넘어간다
            cur_index += 1;

        # 인덱스 초과하면
        if (cur_index == len(food_times)):
            cur_index = 0;

    # print(answer);

    return answer;

# food_times = [3, 1, 1, 1, 2, 4, 3];
# k = 12;

# solution(food_times, k);
"""

# 부스트캠프 이후 작성 코드
def getRemainFoodList(startFoodList : list, diff : int) -> list:
    return list(map(lambda k : max(k - diff, 0), startFoodList));

def checkPossible(startFoodList : list, endTime : int, startFoodSum : int, diff : int) -> bool:
    return (startFoodSum - sum(getRemainFoodList(startFoodList, diff)) <= endTime);

def getAnswer(remainFoodList : list, lastRemainFoodIdx : int, totalLoopCnt : int) -> int:
    curLoopCnt = 0;
    
    # print(remainFoodList);
    # print(totalLoopCnt);
    
    for remainFoodIdx in range(len(remainFoodList)):
        # print(remainFoodIdx);
        
        if (remainFoodList[remainFoodIdx] > 0):
            curLoopCnt += 1;
            
            if (curLoopCnt == totalLoopCnt):
                return (remainFoodIdx + 1);
        
    return -1;

def solution(food_times : list, k : int) -> int:
    startFoodSum = sum(food_times);
    
    if (startFoodSum <= k):
        return -1;
    
    if (len(food_times) > k):
        return (k + 1);
    
    (diff, left, right) = (0, 0, max(food_times));
    
    while (left <= right):
        mid = (left + right) // 2;
        mappedFoodList = list(map(lambda mapK : (mapK - mid), food_times));
        filteredFoodList = list(filter(lambda filterK : (filterK < 0), mappedFoodList));
        ingestedFoodSum = (len(food_times) * mid) + sum(filteredFoodList);
        
        # print(mid, ingestedFoodSum, left, right);
        
        # if (checkPossible(food_times, k, startFoodSum, mid)):
        if (ingestedFoodSum <= k):
            (diff, left) = (mid, mid + 1);
        else:
            right = mid - 1;
    
    remainFoodList = getRemainFoodList(food_times, diff);

    # print(remainFoodList);
    
    return getAnswer(remainFoodList, -1, k + sum(remainFoodList) - startFoodSum + 1);
