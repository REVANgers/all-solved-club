"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        (curNode, visitSet) = (p, set());
        
        while (curNode):
            visitSet.add(curNode);
            curNode = curNode.parent;
            
        # print(visitSet);
        
        curNode = q;
        
        while (curNode):
            if (curNode in visitSet):
                break;
                
            curNode = curNode.parent;
            
        return curNode;
