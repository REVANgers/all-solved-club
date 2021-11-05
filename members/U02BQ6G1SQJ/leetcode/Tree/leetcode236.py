# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(curNode : 'TreeNode', parentNode : 'TreeNode', curLevel : int, parentDict : dict, levelDict : dict) -> None:
    if (not curNode):
        return None;
    
    (parentDict[curNode], levelDict[curNode]) = (parentNode, curLevel);
    dfs(curNode.left, curNode, curLevel + 1, parentDict, levelDict);
    dfs(curNode.right, curNode, curLevel + 1, parentDict, levelDict);
    return None;

def findLCA(node1 : 'TreeNode', node2 : 'TreeNode', parentDict : dict, levelDict : dict) -> 'TreeNode':
    while (node1 != node2):
        # print(node1.val, node2.val);
        
        if (levelDict[node1] > levelDict[node2]):
            node1 = parentDict[node1];
        elif (levelDict[node1] < levelDict[node2]):
            node2 = parentDict[node2];
        else:
            (node1, node2) = (parentDict[node1], parentDict[node2]);

    return node1;

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        (parentDict, levelDict) = (dict(), dict());
        
        dfs(root, None, 0, parentDict, levelDict);
        
        # print(parentDict[p], parentDict[q]);
        # print(levelDict[p], levelDict[q]);
        
        return findLCA(p, q, parentDict, levelDict);
