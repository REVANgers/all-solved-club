# 문제 이해 reference : https://kihyunkimlee.github.io/2021/04/24/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%99%EA%B5%B4-%ED%83%90%ED%97%98/
# 문제 해설 reference : https://tech.kakao.com/2020/07/01/2020-internship-test/
# 위상 정렬 reference : https://hongjw1938.tistory.com/41

import collections;

ROOT = 0;

class TreeNode:
    def __init__(self, idx = 0, isClosed = False, parent = None, childList = list()):
        self.idx = idx;
        self.isClosed = isClosed;
        self.parent = parent;
        self.childList = childList;
        
    def printTreeNode(self):
        print("idx :", self.idx);
        print("isClosed :", self.isClosed);
        print("parent :", self.parent);
        print("childList :", self.childList);
        return None;
    
def printTree(tree : list) -> None:
    for curNode in tree:
        curNode.printTreeNode();
    
    return None;
    
def makeTree(curNode : int, parent : int, adjList : list, tree : list, isVisitedList : list) -> TreeNode:
    isVisitedList[curNode] = True;
    childList = [];
    
    for childNode in adjList[curNode]:
        if (isVisitedList[childNode]):
            continue;
        else:
            childList.append(childNode);
            tree[childNode] = makeTree(childNode, curNode, adjList, tree, isVisitedList);
        
    return TreeNode(curNode, False, parent, childList);
    
def checkVisit(tree : list, curNode : int, endNode : int) -> bool:
    if (curNode == endNode):
        return True;
    
    for nextNode in tree[curNode].childList:
        if (tree[nextNode].isClosed):
            continue;
            
        if (checkVisit(tree, nextNode, endNode)):
            return True;
        
    return False;
    
def checkTree(tree : list, orderDict : dict) -> bool:
    for (key, val) in orderDict.items():
        if (checkVisit(tree, ROOT, key)):
            # print(ROOT, key);

            tree[val].isClosed = False;
            del orderDict[key];
            return False;
        
    return True;
    
def makeDirectGraph(curNode : int, adjList : list, indegreeCntList : list, isVisitedList : list) -> None:
    isVisitedList[curNode] = True;
    
    for nextNode in adjList[curNode]:
        adjList[nextNode].remove(curNode);
        indegreeCntList[nextNode] += 1;
        makeDirectGraph(nextNode, adjList, indegreeCntList, isVisitedList);
    
    return None;
    
def topologySort(nodeCnt : int, adjList : list, indegreeCntList : list) -> bool:
    (dq, visitSet) = (collections.deque([ROOT]), set());
    
    while (dq):
        curNode = dq.popleft();
        visitSet.add(curNode);
        
        for nextNode in adjList[curNode]:
            indegreeCntList[nextNode] -= 1;
            
            if (indegreeCntList[nextNode] == 0):
                dq.append(nextNode);
    
    return (nodeCnt == len(visitSet));
    
def solution(n : int, path : list, order : list) -> bool:
    """
    # 1. 직접 트리를 구성하여 순회 -> 시간 초과
    (adjList, tree, orderDict) = ([[] for _ in range(n)], [None for _ in range(n)], dict(order));
    
    for (src, dst) in path:
        adjList[src].append(dst);
        adjList[dst].append(src);
    
    tree[ROOT] = makeTree(ROOT, -1, adjList, tree, [False for _ in range(n)]);
    
    for (key, val) in orderDict.items():
        if (val == 0):
            return False;
        
        tree[val].isClosed = True;
    
    # print(adjList);
    # print(orderDict);
    
    while (orderDict):
        if (checkTree(tree, orderDict)):
            return False;

        # printTree(tree);
    
    return True;
    """
    
    # 2. 위상 정렬로 사이클 판별
    (adjList, indegreeCntList) = ([set() for _ in range(n)], [0 for _ in range(n)]);
    
    for (src, dst) in path:
        adjList[src].add(dst);
        adjList[dst].add(src);
        
    makeDirectGraph(ROOT, adjList, indegreeCntList, [False for _ in range(n)]);
    
    for (src, dst) in order:
        if (dst == ROOT):
            return False;
        
        if (dst in adjList[src]):
            continue;
        
        adjList[src].add(dst);
        indegreeCntList[dst] += 1;
    
    # for curNode in range(n):
    #     print(curNode, adjList[curNode], indegreeCntList[curNode]);
    
    return topologySort(n, adjList, indegreeCntList);
