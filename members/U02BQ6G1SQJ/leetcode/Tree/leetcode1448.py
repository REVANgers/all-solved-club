# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findGoodNodes(curNode : TreeNode, maxVal : int) -> int:
    goodNodeCnt = 0;
    
    if (curNode.left):
        goodNodeCnt += findGoodNodes(curNode.left, max(maxVal, curNode.left.val));
        
    if (curNode.right):
        goodNodeCnt += findGoodNodes(curNode.right, max(maxVal, curNode.right.val));
        
    return (goodNodeCnt if (curNode.val < maxVal) else goodNodeCnt + 1);

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return findGoodNodes(root, root.val);
