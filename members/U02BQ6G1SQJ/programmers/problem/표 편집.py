# 소요 시간 : 65분
class LinkNode:
    def __init__(self, idx, up = None, down = None):
        self.idx = idx;
        self.up = up;
        self.down = down;
        
    def printLinkNode(self):
        print("idx :", self.idx);
        
        if (self.up):
            print("up :", self.up.idx);
            
        if (self.down):
            print("down :", self.down.idx);
            
        print();
        
        return None;

def printAllLinkNode(head : LinkNode, tail : LinkNode) -> None:
    curNode = head;
    
    while (curNode):
        curNode.printLinkNode();
        curNode = curNode.down;
        
    return None;
    
def printLinkNodeList(linkNodeList : list) -> None:
    for (linkNode, existResult) in linkNodeList:
        print(linkNode.idx, existResult);
    
    print();
    
    return None;
    
def insertLinkNode(tail : LinkNode, idx : int) -> LinkNode:
    insertNode = LinkNode(idx, tail.up, tail);
    (tail.up.down, tail.up) = (insertNode, insertNode);
    return insertNode;
    
def deleteLinkNode(tail : LinkNode, linkNodePtr : int, linkNodeList : list, stack : list) -> int:
    deleteNode = linkNodeList[linkNodePtr][0];
    (deleteNode.up.down, deleteNode.down.up) = (deleteNode.down, deleteNode.up);
    linkNodeList[linkNodePtr][1] = "X";
    stack.append(deleteNode);
    return (deleteNode.up.idx if (deleteNode.down == tail) else deleteNode.down.idx);

def restoreLinkNode(restoreNode : LinkNode, linkNodeList : list) -> None:
    (restoreNode.up.down, restoreNode.down.up) = (restoreNode, restoreNode);
    linkNodeList[restoreNode.idx][1] = "O";
    return None;

def moveUp(head : LinkNode, startNode : LinkNode, moveCnt : int) -> int:
    curNode = startNode;
    
    # curNode.printLinkNode();
    
    for moveIdx in range(moveCnt):
        if (curNode.up == head):
            break;
            
        curNode = curNode.up;
            
    # curNode.printLinkNode();        
    
    return curNode.idx;
    
def moveDown(tail : LinkNode, startNode : LinkNode, moveCnt : int) -> int:
    curNode = startNode;
    
    # curNode.printLinkNode();
    
    for moveIdx in range(moveCnt):
        if (curNode.down == tail):
            break;
            
        curNode = curNode.down;
        
    # curNode.printLinkNode();
            
    return curNode.idx;

def solution(n, k, cmd):
    (linkNodeList, stack) = ([], []);
    (head, tail) = (LinkNode(-1, None, None), LinkNode(n, None, None));
    (head.down, tail.up) = (tail, head);
    
    # head.printLinkNode();
    # tail.printLinkNode();
    
    for insertIdx in range(n):
        linkNodeList.append([insertLinkNode(tail, insertIdx), "O"]);
        
    linkNodePtr = k;
    
    # print(linkNodeList);
    # linkNodeList[ptr][0].printLinkNode();
    # printAllLinkNode(head, tail);
    
    for cmdStr in cmd:
        cmdArr = cmdStr.split(" ");
        
        # print(cmdArr);
        
        # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        if (cmdArr[0] == "U"):
            linkNodePtr = moveUp(head, linkNodeList[linkNodePtr][0], int(cmdArr[1]));
        # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        elif (cmdArr[0] == "D"):
            linkNodePtr = moveDown(tail, linkNodeList[linkNodePtr][0], int(cmdArr[1]));
        # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 
        # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif (cmdArr[0] == "C"):
            linkNodePtr = deleteLinkNode(tail, linkNodePtr, linkNodeList, stack);
        # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 
        # 단, 현재 선택된 행은 바뀌지 않습니다.
        elif (cmdArr[0] == "Z"):
            restoreLinkNode(stack.pop(), linkNodeList);
        
        # print("linkNodePtr :", linkNodePtr);
        # printLinkNodeList(linkNodeList);
    
    return "".join([k[1] for k in linkNodeList]);
