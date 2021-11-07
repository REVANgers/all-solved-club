"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

def dfs(curNode : 'Node', nodeDict : dict) -> None:
    if (not curNode):
        return None;
    
    nodeDict[curNode.val] = curNode;
    dfs(curNode.left, nodeDict);
    dfs(curNode.right, nodeDict);
    return None;

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if (not root):
            return None;
        
        nodeDict = dict();
        
        dfs(root, nodeDict);
        
        sortedKeyList = sorted(nodeDict.keys());
        
        # print(nodeDict);
        # print(sortedKeyList);
        
        for keyIdx in range(len(sortedKeyList) - 1):
            (nodeDict[sortedKeyList[keyIdx]].right, nodeDict[sortedKeyList[keyIdx + 1]].left) = (nodeDict[sortedKeyList[keyIdx + 1]], nodeDict[sortedKeyList[keyIdx]]);
 
        (nodeDict[sortedKeyList[0]].left, nodeDict[sortedKeyList[-1]].right) = (nodeDict[sortedKeyList[-1]], nodeDict[sortedKeyList[0]]);
        return nodeDict[sortedKeyList[0]];
