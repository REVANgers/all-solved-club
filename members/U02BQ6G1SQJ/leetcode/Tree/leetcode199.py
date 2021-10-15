# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preOrder(curNode : TreeNode, rightSideDict : dict, level : int) -> None:
    if (not curNode):
        return None;
    
    rightSideDict[level] = curNode.val;
    preOrder(curNode.left, rightSideDict, level + 1);
    preOrder(curNode.right, rightSideDict, level + 1);
    return None;

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return [];
        
        rightSideDict = dict();
        preOrder(root, rightSideDict, 0);
        
        # print(rightSideDict);
        
        return [rightSideDict[k] for k in sorted(rightSideDict.keys())];
