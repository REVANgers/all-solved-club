# 소요 시간 : 100분
# 카카오 공식 문제 풀이를 먼저 확인한 후, 해설 내용에 맞게 코드를 구현했습니다. 
# 문제 풀이 reference : https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/
import math;
import sys;

MAX_RECURSION_LIMIT = 200000;

class TreeNode:
    def __init__(self, idx = -1, val = 0, left = None, right = None):
        self.idx = idx;
        self.val = val;
        self.left = left;
        self.right = right;
        
    def printTreeNode(self):
        print("idx :", self.idx);
        print("val :", self.val);
        
        if (self.left):
            print("left :", self.left.idx);
            
        if (self.right):
            print("right :", self.right.idx);
            
        return None;
    
def makeBinaryTree(curIdx : int, numList : list, linkList : list, treeNodeList : list) -> TreeNode:
    (leftIdx, rightIdx) = linkList[curIdx];
    
    # print(leftIdx, rightIdx);
    
    leftSubTree = (None if (leftIdx == -1) else makeBinaryTree(leftIdx, numList, linkList, treeNodeList));
    rightSubTree = (None if (rightIdx == -1) else makeBinaryTree(rightIdx, numList, linkList, treeNodeList));
    return TreeNode(curIdx, numList[curIdx], leftSubTree, rightSubTree);
    
def inorder(curNode : TreeNode) -> list:
    if (not curNode):
        return [];
    
    left = inorder(curNode.left);
    right = inorder(curNode.right);
    return (left + [curNode.idx] + right);

def checkPossible(maxGroupSize : int, curNode : TreeNode, dp : list) -> bool:
    if ((not curNode.left) and (not curNode.right)):
        dp[curNode.idx] = (1, curNode.val);
        return True;
        
    if (not curNode.right):
        if (not checkPossible(maxGroupSize, curNode.left, dp)):
            return False;
        
        leftIdx = curNode.left.idx;
        totalList = [dp[leftIdx][0], curNode.val + dp[leftIdx][1]];
        
        if (totalList[1] <= maxGroupSize):
            dp[curNode.idx] = (totalList[0], totalList[1]);
            return True;
        
        if (curNode.val <= maxGroupSize):
            dp[curNode.idx] = (totalList[0] + 1, curNode.val);
            return True;
        
        return False;
        
    if (not curNode.left):
        if (not checkPossible(maxGroupSize, curNode.right, dp)):
            return False;
        
        rightIdx = curNode.right.idx;
        totalList = [dp[rightIdx][0], curNode.val + dp[rightIdx][1]];
        
        if (totalList[1] <= maxGroupSize):
            dp[curNode.idx] = (totalList[0], totalList[1]);
            return True;
        
        if (curNode.val <= maxGroupSize):
            dp[curNode.idx] = (totalList[0] + 1, curNode.val);
            return True;
        
        return False;
        
    # v번 노드에 대해, 다음 4가지 상황이 존재할 수 있습니다. 
    # v번 노드의 왼쪽 자식 노드를 i, 오른쪽 자식 노드를 j라고 하면,
    if (not checkPossible(maxGroupSize, curNode.left, dp)):
        return False;
    
    if (not checkPossible(maxGroupSize, curNode.right, dp)):
        return False;
    
    (leftIdx, rightIdx) = (curNode.left.idx, curNode.right.idx);
    totalList = [dp[leftIdx][0] + dp[rightIdx][0], curNode.val + dp[leftIdx][1] + dp[rightIdx][1]];

    # (1) num[v] + dp[i][1] + dp[j][1] ≤ L 이면, v번 노드와 i번 노드, j번 노드가 속한 그룹을 모두 합해도 가중치 합이 L을 초과하지 않습니다. 
    # 즉 다음과 같이 할 수 있습니다.
    # dp[v][0] = dp[i][0] + dp[j][0] - 1
    # dp[v][1] = num[v] + dp[i][1] + dp[j][1]
    if (totalList[1] <= maxGroupSize):
        dp[curNode.idx] = (totalList[0] - 1, totalList[1]);
        return True;

    # (2) 조건 (1)에 해당하지 않고, (num[v] + dp[i][1] ≤ L) OR (num[v] + dp[j][1] ≤ L) 이면, 두 자식 노드가 속한 그룹들 중 하나의 그룹만 v번 노드와 합칠 수 있습니다. 
    # 이때 dp[v][1] 을 최소로 유지할 수 있는 자식 노드 그룹과 합칩니다.
    # dp[v][0] = dp[i][0] + dp[j][0]
    # dp[v][1] = num[v] + min(dp[i][1], dp[j][1])
    if ((curNode.val + dp[leftIdx][1] <= maxGroupSize) or (curNode.val + dp[rightIdx][1] <= maxGroupSize)):
        dp[curNode.idx] = (totalList[0], curNode.val + min(dp[leftIdx][1], dp[rightIdx][1]));
        return True;

    # (3) 조건 (1), (2)에 해당하지 않고, num[v] ≤ L 이면 양쪽 노드를 모두 잘라야 합니다.
    # dp[v][0] = dp[i][0] + dp[j][0] + 1
    # dp[v][1] = num[v]
    if (curNode.val <= maxGroupSize):
        dp[curNode.idx] = (totalList[0] + 1, curNode.val);
        return True;

    # (4) 조건 (1), (2), (3)에 모두 해당하지 않을 경우, v번 노드만 포함하는 그룹의 크기가 L보다 크므로 최대 그룹 인원이 L 이하가 되도록 트리를 k개 이하의 그룹으로 자를 수 없습니다.
    return False;

def solution(k : int, num : list, links : list) -> int:
    sys.setrecursionlimit(MAX_RECURSION_LIMIT);
    treeNodeList = [None for _ in range(len(num))];
    nonRootNodeSet = set();
    
    for (src, dst) in links:
        if (src != -1):
            nonRootNodeSet.add(src);
            
        if (dst != -1):
            nonRootNodeSet.add(dst);
            
    rootIdx = list(set([k for k in range(len(num))]) - nonRootNodeSet)[0];
    rootNode = makeBinaryTree(rootIdx, num, links, treeNodeList);
    
    # print(rootIdx);
    # rootNode.printTreeNode();
    # print(inorder(rootNode));

    # 트리를 k개 그룹으로 나누었을 때, 최대 그룹의 가중치 합이 (전체 가중치 합) / k보다 작을 수는 없기 때문에, 가능한 L 값의 범위는 다음과 같습니다.
    # (전체 가중치 합) / k ≤ L ≤ (전체 가중치 합)
    # 이 범위에서 파라메트릭 서치를 진행해서 L 값을 찾아내면 됩니다.
    (maxGroupSize, left, right) = (0, max(num), sum(num));
    
    # 파라메트릭 서치는 이분 탐색과 유사한 아이디어로, 이 문제와 같은 최적화 문제를 결정 문제로 바꾸어 푸는 데 사용됩니다.
    # 주어진 최적화 문제: “트리를 k개 이하의 그룹으로 나누어서 얻을 수 있는 최소한의 최대 그룹의 크기는 얼마인가?”
    # 변경된 결정 문제: “트리를 k개 이하의 그룹으로 나누어서 얻을 수 있는 최대 그룹의 크기가 L 이하가 되도록 할 수 있는가?”
    # 위와 같이 문제를 변형하면, L의 최댓값을 이진 탐색을 통해 찾을 수 있습니다. 
    while (left <= right):
        mid = (left + right) // 2;
        # 최대 그룹 인원이 L 이하가 되도록 트리를 자를 때, 필요한 그룹의 수가 k개 이하인지 판별하기 위해 다음과 같은 테이블을 정의합니다.
        # dp[i][0] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 하기 위한 최소 그룹의 수
        # dp[i][1] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 dp[i][0]개로 나누었을 때, i번 노드가 포함되는 서브트리의 가중치 합의 최솟값
        # 예를 들어, 입출력 예 #1과 같이 트리가 구성되어 있고 L = 40일 경우,
        # dp[7][0] = 2, dp[7][1] = 37, dp[9][0] = 3, dp[9][1] = 35 입니다.
        dp = [[0, 0] for _ in range(len(num))];
        
        # print(left, right, mid);
        # print(checkPossible(mid, rootNode, dp));
        
        # 결정 문제의 답이 “Yes”인 최대의 L 값이 문제의 답이 됩니다.
        if ((checkPossible(mid, rootNode, dp)) and (dp[rootIdx][0] <= k)):
            (maxGroupSize, right) = (mid, mid - 1);
        else:
            left = mid + 1;
            
        # print(dp);
    
    return maxGroupSize;
