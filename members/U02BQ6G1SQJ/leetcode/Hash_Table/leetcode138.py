"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (not head):
            return None;
        
        (nodeCnt, curNode, nodeDict, nodeList) = (0, head, dict(), []);
        
        while (curNode):
            nodeList.append(Node(curNode.val, None, None));
            nodeDict[curNode] = nodeCnt;
            (nodeCnt, curNode) = (nodeCnt + 1, curNode.next);
        
        (nodeCnt, curNode) = (0, head);
        
        while (curNode):
            nodeList[nodeCnt].random = (nodeList[nodeDict[curNode.random]] if (curNode.random) else None);
            (nodeCnt, curNode) = (nodeCnt + 1, curNode.next);
        
        for nodeIdx in range(len(nodeList) - 1):
            nodeList[nodeIdx].next = nodeList[nodeIdx + 1];
            
        nodeList[-1].next = None;
        
        # print(nodeDict);
        # print(nodeList);
        
        return nodeList[0];
