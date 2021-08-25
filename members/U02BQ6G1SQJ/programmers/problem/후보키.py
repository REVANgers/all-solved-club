# 시험 당시 작성한 코드 : 실패
"""
# 후보키

from copy import deepcopy;

key_list = [];

def backtrack(cur_col, max_col, cur_key):
    global key_list;

    # 리스트를 인자로 넣어주었을 때 deepcopy!
    new_key = deepcopy(cur_key);

    # print("cur_col : %d, max_col = %d" % (cur_col, max_col));

    # 모두 다 골랐으면
    if (cur_col == max_col):
        # print(new_key);

        # 후보 리스트에 추가
        key_list.append(new_key);

        # print(key_list);

        # 종료
        return;

    # 해당 키를 고르는 경우
    cur_key.append(cur_col);
    backtrack(cur_col + 1, max_col, cur_key);

    # 해당 키를 고르지 않는 경우
    cur_key.remove(cur_col);
    backtrack(cur_col + 1, max_col, cur_key);

    return;

def solution(relation):
    global key_list;

    answer = 0;

    row_cnt = len(relation);
    col_cnt = len(relation[0]);

    # 가능한 모든 후보 키 만들기
    backtrack(0, col_cnt, []);

    # 최소 한 개는 있어야 한다
    key_list.remove([]);

    key_list.sort(key = len);

    print(key_list);

    return answer;

# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]];

# solution(relation);
"""

# 부스트캠프 이후 작성 코드
import itertools;

answerSet = set();

def checkUniqueness(relation : list, keyTuple : tuple) -> None:
    checkSet = set();
    
    for curRecord in relation:
        curStr = "".join([curRecord[int(k)] for k in keyTuple]);
        
        if (curStr in checkSet):
            return None;
        
        checkSet.add(curStr);
        
    # print(checkSet);
    # print(len(checkSet), len(relation));
        
    answerSet.add(keyTuple);
    return None;

def checkMinimality(keyTuple1 : set, keyTuple2 : set):
    (keySet1, keySet2) = (set(keyTuple1), set(keyTuple2));
    intersectionSet = keySet1 & keySet2;
    
    # print("answerSet :", answerSet);
    # print("intersectionSet :", intersectionSet);
    
    if ((intersectionSet == keySet2) and (keyTuple1 in answerSet)):
        # print("keySet2 :", keySet2);
        
        answerSet.remove(keyTuple1);
    elif ((intersectionSet == keySet1) and (keyTuple2 in answerSet)):
        # print("keySet1 :", keySet1);
        
        answerSet.remove(keyTuple2);
    
    return None;

def solution(relation : list) -> int:
    for r in range(1, len(relation[0]) + 1):
        for c in itertools.combinations([k for k in range(len(relation[0]))], r):
            # print(c);
            
            checkUniqueness(relation, c);
    
    for (keyTuple1, keyTuple2) in itertools.combinations(answerSet, 2):
        # print(c);
        
        checkMinimality(keyTuple1, keyTuple2);
            
    # print(answerSet);
    
    return len(answerSet);
