# 소요 시간 : 120분 (실패)
# 문제 풀이 reference : https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
import math;

ROOT = 1;

class TreeNode:
    def __init__(self, idx = 0, sale = 0, childList = []):
        self.idx = idx;
        self.sale = sale;
        self.childList = childList;
        
    def printTreeNode(self):
        print("idx :", self.idx);
        print("sale :", self.sale);
        print("childList :", self.childList);
        print();
        return None;

def printTreeNodeList(treeNodeList : list) -> None:
    for curTreeNode in treeNodeList:
        curTreeNode.printTreeNode();
    
    return None;
    
def getAnswer(treeNodeList : list, dp : list, sumChildList : list, curNode : int, flag : int) -> int:
    if (dp[curNode][flag] != math.inf):
        return dp[curNode][flag];
    
    # 보조 배열 sum_child를 이용하면, d를 구할 수 있습니다.
    dpValue = 0;
    
    if (flag == 0):
        (saleDiff, isAttended) = (math.inf if (treeNodeList[curNode].childList) else 0, False);
        
        for nextNode in treeNodeList[curNode].childList:
            # d[i][0]는 경우를 2가지로 나누어서 생각해야 합니다.
            (saleSum0, saleSum1) = (getAnswer(treeNodeList, dp, sumChildList, nextNode, 0), getAnswer(treeNodeList, dp, sumChildList, nextNode, 1));
            
            if (saleSum0 > saleSum1):
                # d[k][0] > d[k][1] 를 만족하는 k개가 한 개라도 있다면 : 
                # sum_child[i]를 구하는 과정에서 d[k][1]가 적어도 한 번은 더해졌다는 의미가 됩니다. 
                # 즉, i의 자식 노드 중에서 워크숍에 참석한 노드가 있으므로, 문제의 조건을 만족합니다.
                isAttended = True;
            else:
                # d[k][0] > d[k][1] 를 만족하는 k개가 한 개도 없다면 : 
                # sum_child[i]를 구하는 과정에서 d[k][1]가 한 번도 더해지지 않았다는 의미가 됩니다. 
                # 즉, i의 자식 노드 중에서 워크숍에 참석한 노드가 없으므로, 강제로 하나의 노드를 참석시켜야 합니다. 
                # 이때, 가능하면 d[k][1] - d[k][0]의 값이 최소인 k를 참석시키는 것이 좋습니다. 
                # 즉, 매출 손해가 가장 작게 발생하도록 k를 선택해서, 워크숍에 참석시키면 문제에서 요구하는 답을 얻을 수 있습니다.
                saleDiff = min(saleSum1 - saleSum0, saleDiff);
                
            sumChildList[curNode] += min(saleSum0, saleSum1);
        # i의 모든 자식 노드 k에 대해서, d[k][0] > d[k][1] 를 만족하는 k개가 한 개라도 있다면:
        # d[i][0] = sum_child 
        # i의 모든 자식 노드 k에 대해서, d[k][0] > d[k][1] 를 만족하는 k개가 한 개도 없다면:
        # d[i][0] = sum_child + min(d[k][1] - d[k][0])    
        dp[curNode][flag] = (sumChildList[curNode] if (isAttended) else (sumChildList[curNode] + saleDiff));
    else:
        # d[i][1]을 계산하는 방법은 간단합니다. 
        # i가 워크숍에 참석을 했으므로, 자식들이 워크숍에 참석하든 말든, 최소 한 팀에서 한 명 이상 워크숍 참석의 조건을 만족하게 됩니다.
        sumChildList[curNode] = sum([min(getAnswer(treeNodeList, dp, sumChildList, k, 0), getAnswer(treeNodeList, dp, sumChildList, k, 1)) for k in treeNodeList[curNode].childList]);
        # d[i][1] = sales[i] + sum_child
        dp[curNode][flag] = treeNodeList[curNode].sale + sumChildList[curNode];
        
    return dp[curNode][flag];
    
def solution(sales, links):
    (saleList, treeNodeList) = ([0] + sales, [TreeNode(0, 0, [])]);
    
    for saleIdx in range(1, len(saleList)):
        treeNodeList.append(TreeNode(saleIdx, saleList[saleIdx], []));
    
    for (src, dst) in links:
        treeNodeList[src].childList.append(dst);
    
    # print(treeNodeList);
    # printTreeNodeList(treeNodeList);
    
    # 다이나믹 배열을 아래와 같이 정의합니다.
    # d[i][0] : i번 노드가 루트인 서브트리에서, i번 노드가 워크숍에 불참하는 경우의 최적해
    # d[i][1] : i번 노드가 루트인 서브트리에서, i번 노드가 워크숍에 참석하는 경우의 최적해
    # 이렇게 배열 d를 정의했다면, 이 문제에서 요구하는 답은 min(d[1][0], d[1][1])입니다.
    dp = [[math.inf, math.inf] for _ in range(len(sales) + 1)];
    
    # 그러면 다이나믹 배열 d를 어떻게 구할 수 있는지 알아보겠습니다. 
    # 편의를 위해, 보조 배열 sum_child를 다음과 같이 구해놓습니다.
    # sum_child[i] = sum(min(d[k][0] , d[k][1])) {i의 모든 자식 노드 k에 대해서}
    sumChildList = [0 for _ in range(len(sales) + 1)];
    
    return min(getAnswer(treeNodeList, dp, sumChildList, ROOT, 0), getAnswer(treeNodeList, dp, sumChildList, ROOT, 1));
