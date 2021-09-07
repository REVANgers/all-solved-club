# 시험 당시 작성한 코드 : 실패
"""
# 길 찾기 게임

from operator import itemgetter;

def solution(nodeinfo):
    answer = [[]];

    # 실제 트리 정보
    # x축, 높이, 왼쪽 자식, 오른쪽 자식
    # 없으면 -1
    tree = [[]];

    # y축 높이 순서대로 오름차순 정렬
    # 그 다음으로는 x축 기준 왼쪽부터 정렬
    nodeinfo.sort(key = itemgetter(1, 0));

    print(nodeinfo);

    # 루트의 높이는 1
    cur_h = 1;

    # 이전 높이의 index
    prev_index = 0;

    # 현재 높이의 index
    cur_index = 1;

    # 루트는 지정
    # x축, 높이, 왼쪽 자식, 오른쪽 자식
    tree.append([nodeinfo[0][0], cur_h, -1, -1]);

    # 실제 tree 만들기
    for i in range(1, len(nodeinfo)):
        # 현재 노드 불러오기
        cur_node = nodeinfo[i];

    return answer;

# nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]];

# solution(nodeinfo);
"""

# 부스트캠프 이후 작성 코드
import sys;

MAX_NODE_CNT = 10000;

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val;
        self.left = left;
        self.right = right;
        
    def printTreeNode(self):
        print(self.val, self.left, self.right);   
        return None;
        
def makeBinaryTree(nodeList : list) -> TreeNode:
    if (len(nodeList) == 0):
        return None;
    elif (len(nodeList) == 1):
        return TreeNode(nodeList[0][0], None, None);

    yList = [k[2] for k in nodeList];
    rootIdx = yList.index(max(yList));
    rootNode = nodeList[rootIdx];
    left = makeBinaryTree(list(filter(lambda k : (k[1] < rootNode[1]), nodeList)));
    right = makeBinaryTree(list(filter(lambda k : (k[1] > rootNode[1]), nodeList)));
    return TreeNode(rootNode[0], left, right);
    
def preorder(curNode : TreeNode) -> list:
    if (curNode == None):
        return [];
    
    left = preorder(curNode.left);
    right = preorder(curNode.right);
    return ([curNode.val] + left + right);

def postorder(curNode : TreeNode) -> list:
    if (curNode == None):
        return [];
    
    left = postorder(curNode.left);
    right = postorder(curNode.right);
    return (left + right + [curNode.val]);
    
def solution(nodeinfo : list) -> list:
    sys.setrecursionlimit(MAX_NODE_CNT);
    nodeList = [([k + 1] + nodeinfo[k]) for k in range(len(nodeinfo))];
    rootNode = makeBinaryTree(nodeList);
    
    # print(nodeList);
    # rootNode.printTreeNode();
    
    return [preorder(rootNode), postorder(rootNode)];
