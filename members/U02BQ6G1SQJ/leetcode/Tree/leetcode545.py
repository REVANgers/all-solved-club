# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(curNode : Optional[TreeNode], parentDict : dict) -> None:
    if (curNode.left):
        parentDict[curNode.left] = curNode;
        dfs(curNode.left, parentDict);
    
    if (curNode.right):
        parentDict[curNode.right] = curNode;
        dfs(curNode.right, parentDict);
        
    return None;
    
def findLeafBoundary(curNode : Optional[TreeNode]) -> List[TreeNode]:
    if ((curNode.left) and (curNode.right)):
        return (findLeafBoundary(curNode.left) + findLeafBoundary(curNode.right));
    elif (curNode.left):
        return findLeafBoundary(curNode.left);
    elif (curNode.right):
        return findLeafBoundary(curNode.right);
    
    return [curNode];

def findLeftBoundary(curNode : Optional[TreeNode], parentDict : dict) -> List[TreeNode]:
    return ((findLeftBoundary(parentDict[curNode], parentDict) + [curNode]) if (curNode in parentDict.keys()) else []);

def findRightBoundary(curNode : Optional[TreeNode], parentDict : dict) -> List[TreeNode]:
    return (([curNode] + findRightBoundary(parentDict[curNode], parentDict)) if (curNode in parentDict.keys()) else []);

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return [];
        
        if ((not root.left) and (not root.right)):
            return [root.val];
        
        parentDict = dict();
        
        dfs(root, parentDict);
        leafBoundaryList = findLeafBoundary(root);
        leftBoundaryList = (findLeftBoundary(parentDict[leafBoundaryList[0]], parentDict) if (root.left) else []);
        rightBoundaryList = (findRightBoundary(parentDict[leafBoundaryList[-1]], parentDict) if (root.right) else []);
        
        # print(parentDict);
        # print(leafBoundaryList);
        # print(leftBoundaryList);
        # print(rightBoundaryList);
        
        return [k.val for k in ([root] + leftBoundaryList + leafBoundaryList + rightBoundaryList)];
