# 시험 당시 작성한 코드 : 시간 초과
"""
# 오픈채팅방

def solution(record):
    answer = [];

    # 유저 아이디 모은 배열
    uid_list = [];
    
    # 닉네임 모은 배열
    nn_list = [];

    # 최종 아이디 기록
    for i in range(len(record)):
        # 공백 기준으로 나누기
        record[i] = record[i].split(' ');

        # print(record[i]);

        # Enter, Leave, Change
        cmd = record[i][0];

        # 유저 아이디
        uid = record[i][1];

        # 입장
        if (cmd == 'Enter'):
            # 닉네임
            nn = record[i][2];

            # 이미 있는 uid이면
            if (uid in uid_list):
                # 그 위치를 가지고 와서
                uid_index = uid_list.index(uid);
                
                # 닉네임을 바꿔준다
                nn_list[uid_index] = nn;

            # 새로운 uid이면
            else:
                # 유저 아이디 추가
                uid_list.append(uid);

                # 닉네임 추가
                nn_list.append(nn);

        # 변경
        elif (cmd == 'Change'):
            # 닉네임
            nn = record[i][2];

            # 그 위치를 가지고 와서
            uid_index = uid_list.index(uid);

            # 닉네임을 바꿔준다
            nn_list[uid_index] = nn;

    # 그대로 출력
    for i in range(len(record)):
        # print(record[i]);

        # Enter, Leave, Change
        cmd = record[i][0];

        # 유저 아이디
        uid = record[i][1];

        # 입장
        if (cmd == 'Enter'):
            # 그 위치를 가지고 와서
            uid_index = uid_list.index(uid);

            # 닉네임과 함께 넣어준다
            answer.append("%s님이 들어왔습니다." % nn_list[uid_index]);

        # 퇴장
        elif (cmd == 'Leave'):
            # 그 위치를 가지고 와서
            uid_index = uid_list.index(uid);

            # 닉네임과 함께 넣어준다
            answer.append("%s님이 나갔습니다." % nn_list[uid_index]);

    # print(uid_list);
    # print(nn_list);

    # print(answer);

    return answer;

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"];

# solution(record)
"""

# 부스트캠프 이후 작성 코드
def solution(record : list) -> list:
    (answerList, recordDict) = ([], dict());
    
    for recordStr in record:
        recordArr = recordStr.split();
        
        if (recordArr[0] == "Enter"):
            recordDict[recordArr[1]] = recordArr[2];
            answerList.append([recordArr[1], "님이 들어왔습니다."]);
        elif (recordArr[0] == "Leave"):
            answerList.append([recordArr[1], "님이 나갔습니다."]);
        elif (recordArr[0] == "Change"):
            recordDict[recordArr[1]] = recordArr[2];
    
    return ["".join([recordDict[uid], msg]) for (uid, msg) in answerList];
