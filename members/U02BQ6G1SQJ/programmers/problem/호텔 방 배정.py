# Segment Tree Reference : https://www.acmicpc.net/blog/view/9
# 문제 해설 Reference : https://tech.kakao.com/2020/04/01/2019-internship-test/

# import math;
import sys;

MAX_ROOM_NUMBER = 200000;

# 다음과 같은 과정을 거쳐서 Segment Tree를 만들 수 있습니다.
# segmentList : 세그먼트 트리로 만들 리스트
# tree : 세그먼트 트리
# node : 세그먼트 트리 노드 번호
# node가 담당하는 합의 범위가 start ~ end
def initSegmentTree(segmentList : list, segmentTree : list, node : int, start : int, end : int) -> int:
    # start == end 인 경우는 node가 리프 노드인 경우입니다. 
    # 리프 노드는 배열의 그 원소를 가져야 하기 때문에 segmentTree[node] = segmentList[start]가 됩니다.
    if (start == end):
        segmentTree[node] = segmentList[start];
    # node의 왼쪽 자식은 node * 2, 오른쪽 자식은 node * 2 + 1이 됩니다. 
    # 또, node가 담당하는 구간이 [start, end] 라면 왼쪽 자식은 [start, (start + end) // 2], 오른쪽 자식은 [(start + end) // 2 + 1, end]를 담당해야 합니다. 
    # 따라서, 재귀 함수를 이용해서 왼쪽 자식과 오른쪽 자식 트리를 만들고, 그 합을 저장해야 합니다.
    else:
        mid = (start + end) // 2;
        leftInit = initSegmentTree(segmentList, segmentTree, node * 2, start, mid);
        rightInit = initSegmentTree(segmentList, segmentTree, (node * 2) + 1, mid + 1, end);
        segmentTree[node] = (leftInit + rightInit);
        
    return segmentTree[node];

# 구간 left, right이 주어졌을 때, 합을 찾으려면 루트부터 트리를 순회하면서 각 노드가 담당하는 구간과 left, right 사이의 관계를 살펴봐야 합니다.
# node가 담당하고 있는 구간이 [start, end] 이고, 합을 구해야하는 구간이 [left, right] 이라면 다음과 같이 4가지 경우로 나누어질 수 있습니다.
def sumSegmentTree(segmentTree : list, node : int, start : int, end : int, left : int, right : int) -> int:
    # 1. [left, right]와 [start, end]가 겹치지 않는 경우
    # 1번 경우에는 if (left > end or right < start)로 나타낼 수 있습니다. 
    # left > end는 [start, end] 뒤에 [left, right]가 있는 경우이고, right < start는 [start, end] 앞에 [left, right]가 있는 경우입니다. 
    # 이 경우에는 겹치지 않기 때문에, 더 이상 탐색을 이어나갈 필요가 없습니다. 따라서 0을 리턴해 탐색을 종료합니다.
    if ((left > end) or (right < start)):
        return 0;
    
    # 2. [left, right]가 [start, end]를 완전히 포함하는 경우
    # 2번 경우는 if (left <= start and right >= end)로 나타낼 수 있습니다. 
    # 이 경우도 더 이상 탐색을 이어나갈 필요가 없습니다. 
    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고, 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적입니다. 
    # 따라서, segmentTree[node]를 리턴해 탐색을 종료합니다.
    if ((left <= start) and (right >= end)):
        return segmentTree[node];
    
    # 3. [start, end]가 [left, right]를 완전히 포함하는 경우
    # 4. [left, right]와 [start, end]가 겹쳐져 있는 경우 (1, 2, 3 제외한 나머지 경우)
    # 3번과 4번의 경우에는 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 합니다.
    mid = (start + end) // 2;
    leftSum = sumSegmentTree(segmentTree, node * 2, start, mid, left, right);
    rightSum = sumSegmentTree(segmentTree, (node * 2) + 1, mid + 1, end, left, right);
    return (leftSum + rightSum);

# 중간에 어떤 수를 변경한다면, 그 숫자가 포함된 구간을 담당하는 노드를 모두 변경해줘야 합니다.
# idx번째 수를 val로 변경한다면, 그 수가 얼마만큼 변했는지를 알아야 합니다. 
# 이 수를 diff라고 하면, diff = val - a[idx]로 쉽게 구할 수 있습니다.
# 수 변경은 2가지 경우가 있습니다.
def updateSegmentTree(segmentTree : list, node : int, start : int, end : int, idx : int, diff : int) -> None:
    # 1. [start, end]에 idx가 포함되지 않는 경우
    # 포함되지 않는 경우는 그 자식도 idx가 포함되지 않기 때문에, 탐색을 중단해야 합니다.
    if ((idx < start) or (idx > end)):
        return None;
    
    # 2. [start, end]에 idx가 포함되는 경우
    # node의 구간에 포함되는 경우에는 diff만큼 증가시켜 합을 변경해 줄 수 있습니다. 
    # tree[node] = tree[node] + diff
    segmentTree[node] += diff;
    mid = (start + end) // 2;
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에, start != end로 리프 노드인지 검사를 해야 합니다.
    if (start != end):
        updateSegmentTree(segmentTree, node * 2, start, mid, idx, diff);
        updateSegmentTree(segmentTree, (node * 2) + 1, mid + 1, end, idx, diff);
    
    return None;

def querySegmentTree(segmentTree : list, node : int, start : int, end : int, left : int, right : int) -> int:
    if ((left > end) or (right < start)):
        return (right + 1);
    
    if ((left <= start) and (right >= end) and (segmentTree[node] == 0)):
        # print("segmentTree[node] :", segmentTree[node], "node :", node);
        # print("start :", start, "end :", end, "left :", left, "right :", right);
        
        return start;
    
    if (start == end):
        return (right + 1);
    
    mid = (start + end) // 2;
    leftQuery = querySegmentTree(segmentTree, node * 2, start, mid, left, right);
    rightQuery = querySegmentTree(segmentTree, (node * 2) + 1, mid + 1, end, left, right);
    
    # print("left :", leftQuery);
    # print("right :", rightQuery);
    
    return min(leftQuery, rightQuery);

def find(node : int, parentDict : dict) -> int:
    if (parentDict[node] != node):
        parentDict[node] = find(parentDict[node], parentDict);
        
    return parentDict[node];

def union(node1 : int, node2 : int, parentDict : dict, rankDict : dict) -> None:
    (root1, root2) = (find(node1, parentDict), find(node2, parentDict));
    
    if (rankDict[root1] < rankDict[root2]):
        parentDict[root1] = root2;
    else:
        parentDict[root2] = root1;
        
        if (rankDict[root1] == rankDict[root2]):
            rankDict[root1] += 1;
    
    return None;

def findRoomNumber(node : int, parentDict : dict) -> int:
    # 먼저 고객에게 배정할 방이 빈 방이면 즉시 배정합니다. 
    if node not in parentDict.keys():
        # 이때, 배정된 방 번호를 노드로 만들어 준 후, 부모 노드는 단순히 현재 방 번호에 1을 더한 값으로 지정합니다.
        parentDict[node] = node + 1;
        return node;
    
    # 만약 고객에게 배정할 방이 빈 방이 아니면 다음과 같이 배정할 빈 방을 탐색합니다.
    # 1. 현재 노드의 방이 빈 방이 아니면 빈 방이 나올 때까지 부모 노드를 계속 방문합니다.
    targetRoomNumber = findRoomNumber(parentDict[node], parentDict);
    # 2. 빈 방이 나오면 고객에게 배정하고, 배정된 방 번호를 노드로 만든 후, 부모 노드는 배정된 방 번호에 1을 더해준 값으로 지정합니다.
    # 3. 빈 방이 나오기 전까지 방문한 노드들의 부모 노드 또한 고객에게 배정한 방 번호에 1을 더한 값으로 수정합니다.
    parentDict[node] = targetRoomNumber + 1;
    return targetRoomNumber;

def solution(k : int, room_number : list) -> list:
    """
    # 1. 시간 복잡도를 고려하지 않은 풀이 : 시간 초과
    (answerList, isVisitedList) = ([0 for _ in range(len(room_number))], [False for _ in range(k + 1)]);
    
    for customerIdx in range(len(room_number)):
        targetRoomNumber = isVisitedList.index(False, room_number[customerIdx]);
        isVisitedList[targetRoomNumber] = True;
        answerList[customerIdx] = targetRoomNumber;
    """
    
    """
    # 2. Segment Tree를 사용한 풀이 : 시간 초과
    answerList = [0 for _ in range(len(room_number))];
    # 만약, N이 2의 제곱꼴인 경우에는 Full Binary Tree 입니다. 
    # 또, 그 때 높이는 logN 입니다. 
    # 리프 노드가 N개인 Full Binary Tree는 필요한 노드의 개수가 2 * N - 1개 입니다.
    # N이 2의 제곱꼴이 아닌 경우에는 높이가 H = (log2)N 이고, 총 세그먼트 트리를 만드는데 필요한 배열의 크기는 2 ^ (H + 1) - 1개가 됩니다.
    segmentTree = [0 for _ in range(2 ** (math.ceil(math.log(k + 1, 2)) + 1))];
    
    initSegmentTree([0 for _ in range(k + 1)], segmentTree, 1, 1, k);
    
    for customerIdx in range(len(room_number)):
        # print("roomNumber :", room_number[customerIdx]);
        
        targetRoomNumber = querySegmentTree(segmentTree, 1, 1, k, room_number[customerIdx], k);
        updateSegmentTree(segmentTree, 1, 1, k, targetRoomNumber, 1);
        answerList[customerIdx] = targetRoomNumber;
        
        # print(segmentTree);
        # print();
    """
    
    # 3. Union-Find를 활용한 풀이
    sys.setrecursionlimit(MAX_ROOM_NUMBER);
    # 이때, 전체 방 개수가 10^12 개 이므로 배열을 이용해 모든 방을 나타낼 경우 메모리가 부족하게 됩니다. 
    # 고객들에게 배정되는 방 개수는 최대 20만 개 이므로, HashMap 등을 이용해서 필요한 만큼 노드를 생성하면 메모리를 절약할 수 있습니다.
    parentDict = dict();
    return [findRoomNumber(curRoomNumber, parentDict) for curRoomNumber in room_number];
